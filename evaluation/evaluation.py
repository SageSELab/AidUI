# https://towardsdatascience.com/evaluating-multi-label-classifiers-a31be83da6ea
import json
import shutil
import numpy as np
from sklearn.metrics import multilabel_confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
import torch
import torchvision.ops.boxes as bops
from config import *
import utils.utils as utils

def set_dp_ground_truth(annotation_file, type, ground_truth_info):
    f = open(annotation_file)
    data = json.load(f)
    for image in data["images"]:
        img_id = image["id"]
        img_filename = image["file_name"].split("/")[1]
        # copy the image to input folder
        src = "./evaluation/evaluation_dataset/" + type + "/images/" + img_filename
        dst = "./input/" + img_filename
        shutil.copyfile(src, dst)
        # create annotation info
        labels = []
        segments = []
        for annotation in data["annotations"]:
            if(annotation["image_id"] == img_id):
                category_id = annotation["category_id"]
                for category in data["categories"]:
                    if(category["id"] == category_id):
                        labels.append(category["name"])
                        segments.append(annotation["bbox"])
        # print(img_filename)
        # print("mobile")
        # print(labels)
        ground_truth_info[img_filename] = {"type": type, "labels": labels, "segments": segments}
    f.close()

def set_evaluation_data():
    evaluation_mobile_dataset_annotation = "./evaluation/evaluation_dataset/mobile/result.json"
    evaluation_web_dataset_annotation = "./evaluation/evaluation_dataset/web/result.json"
    ground_truth_info = {}
    set_dp_ground_truth(evaluation_mobile_dataset_annotation, "mobile", ground_truth_info)
    set_dp_ground_truth(evaluation_web_dataset_annotation, "web", ground_truth_info)
    # utils.print_dictionary(ground_truth_info, "ground_truth_info")
    # print(len(ground_truth_info))
    utils.write_json_file(ground_truth_info, "ground_truth_info")

def get_dp_ground_truth(image_file):
    img_filename = image_file.split("/")[-1]
    ground_truth_filename = "./output/ground_truth_info.json"
    f = open(ground_truth_filename)
    data = json.load(f)
    dp_ground_truth = None
    for filename in data.keys():
        if filename == img_filename:
            dp_ground_truth = data[filename]
    # label binarization
    dps = dp_ground_truth["labels"]
    # print(dps)
    # labels_binarization = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    labels_binarization = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if len(dps) != 0:
        for dp in dps:
            index = class_dp_bin_index[dp]
            labels_binarization[index] = 1
    # print(labels_binarization)
    dp_ground_truth["labels_binarization"] = labels_binarization

    # segment info
    segments = []
    for segment in dp_ground_truth["segments"]:
        column_min = segment[0]
        row_min = segment[1]
        width = segment[2]
        height = segment[3]
        column_max = column_min + width
        row_max = row_min + height
        item = {
            "column_min": column_min
            , "column_max": column_max
            , "row_min": row_min
            , "row_max": row_max
            , "width": width
            , "height": height
        }
        segments.append(item)
    dp_ground_truth["segments"] = segments
    return dp_ground_truth

def init_tp_fp_matrix():
    num_categories = 17
    matrix = []
    for row in range(num_categories):
        matrix.append([0 for column in range(num_categories)])
    return matrix

def set_tp_fp_matrix(dp_predictions_bin, dp_expectations_bin):
    tp_fp_matrix = init_tp_fp_matrix()
    for i in range(len(dp_expectations_bin)):
        prediction = dp_predictions_bin[i]
        ground_truth = dp_expectations_bin[i]
        ground_truth_dp_category_indices = []
        for j in range(len(ground_truth)):
            dp_category_index = j
            if(ground_truth[dp_category_index] == 1):
                ground_truth_dp_category_indices.append(dp_category_index)
                is_tp = (ground_truth[dp_category_index] == 1 and prediction[dp_category_index] == 1)
                if(is_tp):
                    tp_fp_matrix[dp_category_index][dp_category_index] += 1

        for k in range(len(ground_truth)):
            # print(j)
            dp_category_index = k
            is_fp = (ground_truth[dp_category_index] == 0 and prediction[dp_category_index] == 1)
            if(is_fp):
                samplewise_mcm = multilabel_confusion_matrix(dp_expectations_bin, dp_predictions_bin, samplewise=True)
                # print("dp_category_index", dp_category_index)
                # num_tp = samplewise_mcm[0][1][1]
                fp_share = 1 / len(ground_truth_dp_category_indices)
                for row_dp_category_index in ground_truth_dp_category_indices:
                    tp_fp_matrix[row_dp_category_index][dp_category_index] += fp_share
    return tp_fp_matrix

def get_tp_fp_distribution_rounded(tp_fp_matrix):
    numpy_tp_fp_matrix = np.array(tp_fp_matrix)
    # utils.print_array(numpy_tp_fp_matrix)
    # print(numpy_tp_fp_matrix[:,0])
    # print(numpy_tp_fp_matrix[:,1])
    # print(numpy_tp_fp_matrix[:,2])
    # print(numpy_tp_fp_matrix[:,3])

    dp_categorywise_tp_plus_fp = []
    for dp_category_index in range(len(numpy_tp_fp_matrix)):
        # print(numpy_tp_fp_matrix[:,dp_category_index])
        # print(sum(numpy_tp_fp_matrix[:,dp_category_index]))
        dp_categorywise_tp_plus_fp.append(sum(numpy_tp_fp_matrix[:,dp_category_index]))
    numpy_dp_categorywise_tp_plus_fp = np.array(dp_categorywise_tp_plus_fp)
    # print(numpy_dp_categorywise_tp_plus_fp)
    # print(numpy_tp_fp_matrix / numpy_dp_categorywise_tp_plus_fp)
    tp_fp_distribution = numpy_tp_fp_matrix / numpy_dp_categorywise_tp_plus_fp
    np.nan_to_num(tp_fp_distribution, copy=False, nan=0.0)
    tp_fp_distribution_rounded = np.round(tp_fp_distribution, 2)
    return tp_fp_distribution_rounded

def get_classification_evaluation_aggregate_data(dp_predictions, dp_expectations):
    # metrics calculation
    conf_mat = multilabel_confusion_matrix(np.array(dp_expectations), np.array(dp_predictions))
    accuracy = accuracy_score(dp_expectations, dp_predictions)
    precision = precision_score(dp_expectations, dp_predictions, average=None)
    recall = recall_score(dp_expectations, dp_predictions, average=None)
    f1score = f1_score(dp_expectations, dp_predictions, average=None)

    # num of data points and instances
    num_data_points = len(dp_expectations)
    num_instances = np.array(dp_expectations).sum(0)
    num_nodp_data_points = num_instances[16]
    num_nodp_instances = num_instances[16]
    num_dp_data_points = num_data_points - num_nodp_data_points
    num_dp_instances = 0
    for i in range(len(conf_mat) - 1):
        num_dp_instances += num_instances[i]
    num_dp_nodp_instances = num_dp_instances + num_nodp_instances

    # NO DP calculation
    nodp_precision = precision[16]
    nodp_recall = recall[16]
    nodp_f1score = f1score[16]

    # DP weighted avg calculation
    dp_weighted_precisions = []
    dp_weighted_recalls = []
    dp_weighted_f1scores = []
    for i in range(len(conf_mat) - 1):
        dp_weighted_precisions.append(precision[i] * num_instances[i])
        dp_weighted_recalls.append(recall[i] * num_instances[i])
        dp_weighted_f1scores.append(f1score[i] * num_instances[i])
    dp_weighted_avg_precision = sum(dp_weighted_precisions) / num_dp_instances
    dp_weighted_avg_recall = sum(dp_weighted_recalls) / num_dp_instances
    dp_weighted_avg_f1score = sum(dp_weighted_f1scores) / num_dp_instances

    # (DP + NO DP) weighted avg calculation
    dp_nodp_weighted_avg_precision = (dp_weighted_avg_precision * num_dp_instances + nodp_precision * num_nodp_instances) / num_dp_nodp_instances
    dp_nodp_weighted_avg_recall = (dp_weighted_avg_recall * num_dp_instances + nodp_recall * num_nodp_instances) / num_dp_nodp_instances
    dp_nodp_weighted_avg_f1score = (dp_weighted_avg_f1score * num_dp_instances + nodp_f1score * num_nodp_instances) / num_dp_nodp_instances

    # FP count for DP, NO DP
    nodp_num_fp = conf_mat[16][0, 1]
    dp_num_fp = 0
    for i in range(len(conf_mat) - 1):
        dp_num_fp += conf_mat[i][0, 1]
    dp_nodp_num_fp = dp_num_fp + nodp_num_fp

    evaluation_data = {}
    evaluation_data["no_dp"] = {
        "num_data_points": num_nodp_data_points
        , "num_instances": num_nodp_instances
        , "num_fp": nodp_num_fp
        , "precision": nodp_precision
        , "recall": nodp_recall
        , "f1score": nodp_f1score
        }
    evaluation_data["dp"] = {
        "num_data_points": num_dp_data_points
        , "num_instances": num_dp_instances
        , "num_fp": ""
        , "precision": dp_weighted_avg_precision
        , "recall": dp_weighted_avg_recall
        , "f1score": dp_weighted_avg_f1score
        }
    evaluation_data["all"] = {
        "num_data_points": num_data_points
        , "num_instances": num_dp_nodp_instances
        , "num_fp": ""
        , "precision": dp_nodp_weighted_avg_precision
        , "recall": dp_nodp_weighted_avg_recall
        , "f1score": dp_nodp_weighted_avg_f1score
        }
    return evaluation_data

def get_classification_evaluation_data(dp_predictions, dp_expectations):
    # calculate num of instances, confusion matrix, precision, recall for all dp categories
    num_data_points = len(dp_expectations)
    num_dp_instances = np.array(dp_expectations).sum(0)
    conf_mat = multilabel_confusion_matrix(np.array(dp_expectations), np.array(dp_predictions))
    accuracy = accuracy_score(dp_expectations, dp_predictions)
    precision = precision_score(dp_expectations, dp_predictions, average=None)
    recall = recall_score(dp_expectations, dp_predictions, average=None)
    f1score = f1_score(dp_expectations, dp_predictions, average=None)

    precisions = []
    recalls = []
    # populate category_info
    category_info = {}
    for i in range(len(conf_mat)):
        category_info[class_bin_index_to_dp[str(i)]] = {
            "num_instances": str(num_dp_instances[i])
            , "conf_mat": conf_mat[i].tolist()
            , "precision": str(precision[i])
            , "recall": str(recall[i])
            , "f1score": str(f1score[i])
        }
    #     # populate precisions & recalls list
    #     if(num_dp_instances[i] != 0):
    #         precisions.append(precision[i])
    #         recalls.append(recall[i])
    # avg_precision = sum(precisions) / len(precisions)
    # avg_recall = sum(recalls) / len(recalls)

    # populate evaluation_data
    evaluation_data = {}
    evaluation_data["num_data_points"] = str(num_data_points)
    evaluation_data["num_total_dp_instances"] = str(sum(num_dp_instances))
    evaluation_data["category_info"] = category_info
    evaluation_data["macro_avg_precision"] = str(precision_score(dp_expectations, dp_predictions, average="macro"))
    evaluation_data["macro_avg_recall"] = str(recall_score(dp_expectations, dp_predictions, average="macro"))
    evaluation_data["weighted_avg_precision"] = str(precision_score(dp_expectations, dp_predictions, average="weighted"))
    evaluation_data["weighted_avg_recall"] = str(recall_score(dp_expectations, dp_predictions, average="weighted"))
    evaluation_data["accuracy"] = str(accuracy)
    evaluation_data["weighted_avg_f1score"] = str(f1_score(dp_expectations, dp_predictions, average="weighted"))
    evaluation_data["avg_precision"] = evaluation_data["weighted_avg_precision"]
    evaluation_data["avg_recall"] = evaluation_data["weighted_avg_recall"]
    evaluation_data["avg_f1score"] = evaluation_data["weighted_avg_f1score"]
    return evaluation_data

def get_localization_evaluation_data(dp_predictions_segments, dp_expectations_segments, dp_predictions_labels, dp_expectations_labels):
    dp_pred_exp_segments = {}
    for i in range(len(dp_predictions_labels)):
        # if dp_predictions_labels[i][0] != "NO DP":
        predicted_labels = dp_predictions_labels[i]
        expected_labels = dp_expectations_labels[i]
        predicted_segments = dp_predictions_segments[i]
        expected_segments = dp_expectations_segments[i]
        # if(set(predicted_labels) == set(expected_labels)):
        for j in range(len(predicted_labels)):
            if predicted_labels[j] != "NO DP":
                if(predicted_labels[j]) in expected_labels:
                    prediction_index = j
                    expectation_index = expected_labels.index(predicted_labels[j])
                    predicted_segment = predicted_segments[prediction_index]
                    expected_segment = expected_segments[expectation_index]
                    if(predicted_labels[j] in dp_pred_exp_segments.keys()):
                        dp_pred_exp_segments[predicted_labels[j]]["predicted_segments"].append(predicted_segment)
                        dp_pred_exp_segments[predicted_labels[j]]["expected_segments"].append(expected_segment)
                    else:
                        dp_pred_exp_segments[predicted_labels[j]] = {"predicted_segments": [predicted_segment], "expected_segments": [expected_segment]}

    localization_evaluation_data = {"avg_iou": None, "custom_avg_iou": None, "dp_iou_info": {}}
    avg_ious = []
    custom_avg_ious = []
    for key, value in dp_pred_exp_segments.items():
        predicted_segments= value["predicted_segments"]
        expected_segments = value["expected_segments"]
        iou_list = []
        custom_iou_list = []
        for i in range(len(predicted_segments)):
            y_pred = predicted_segments[i]
            y_expected = expected_segments[i]

            # typical IoU calculation
            box1 = torch.tensor([[y_pred["column_min"], y_pred["row_min"], y_pred["column_max"], y_pred["row_max"]]], dtype=torch.float)
            box2 = torch.tensor([[y_expected["column_min"], y_expected["row_min"], y_expected["column_max"], y_expected["row_max"]]], dtype=torch.float)
            iou = bops.box_iou(box1, box2)
            iou_list.append(float(iou))

            # custom IoU calculation
            custom_iou = 0
            if(
                y_expected["column_min"] <= y_pred["column_min"] <= y_expected["column_max"]
                and y_expected["column_min"] <= y_pred["column_max"] <= y_expected["column_max"]
                and y_expected["row_min"] <= y_pred["row_min"] <= y_expected["row_max"]
                and y_expected["row_min"] <= y_pred["row_max"] <= y_expected["row_max"]
            ):
                custom_iou = 1
            else:
                box1 = torch.tensor([[y_pred["column_min"], y_pred["row_min"], y_pred["column_max"], y_pred["row_max"]]], dtype=torch.float)
                box2 = torch.tensor([[y_expected["column_min"], y_expected["row_min"], y_expected["column_max"], y_expected["row_max"]]], dtype=torch.float)
                custom_iou = bops.box_iou(box1, box2)
            custom_iou_list.append(float(custom_iou))

        avg_iou = sum(iou_list) / len(iou_list)
        avg_ious.append(avg_iou)
        # do for custom
        custom_avg_iou = sum(custom_iou_list) / len(custom_iou_list)
        custom_avg_ious.append(custom_avg_iou)

        localization_evaluation_data["dp_iou_info"][key] = {
            "iou_list": iou_list
            , "avg_iou": avg_iou
            , "custom_iou_list": custom_iou_list
            , "custom_avg_iou": custom_avg_iou
        }

    if len(avg_ious) != 0:
        localization_evaluation_data["avg_iou"] = sum(avg_ious) / len(avg_ious)
        # do for custom
        localization_evaluation_data["custom_avg_iou"] = sum(custom_avg_ious) / len(custom_avg_ious)
    else:
        localization_evaluation_data["avg_iou"] = "None"
        # do for custom
        localization_evaluation_data["custom_avg_iou"] = "None"

    return localization_evaluation_data

def evaluate(dp_predictions_bin, dp_expectations_bin, dp_predictions_segments, dp_expectations_segments, dp_predictions_labels, dp_expectations_labels, types, score_threshold_value):
    # sample code
    # -----------
    # y_gt = np.array([[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    # y_predicted = np.array([[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    # confusion_matrix = multilabel_confusion_matrix(y_gt, y_predicted)
    # print(confusion_matrix)

    # confusion matrix format
    # -----------------------
    # TN   FP
    # FN   TP

    # precision, recall formula
    # Precision = TP / (TP + FP)
    # Recall = TP / (TP + FN)

    ########################################
    # for all datapoints
    ########################################

    # classification evaluation
    overall_classification_evaluation_data = get_classification_evaluation_data(dp_predictions_bin, dp_expectations_bin)
    utils.write_json_file(overall_classification_evaluation_data, "overall_classification_evaluation_data_" + str(score_threshold_value))
    utils.print_write_classification_evaluation_result(overall_classification_evaluation_data, "overall_classification_evaluation_data_" + str(score_threshold_value))

    # aggregate evaluation
    overall_classification_evaluation_aggregate_data = get_classification_evaluation_aggregate_data(dp_predictions_bin, dp_expectations_bin)
    utils.print_classification_evaluation_aggregate_result(overall_classification_evaluation_aggregate_data)

    # TP FP Distribution
    tp_fp_matrix = set_tp_fp_matrix(dp_predictions_bin, dp_expectations_bin)
    tp_fp_distribution_rounded = get_tp_fp_distribution_rounded(tp_fp_matrix)
    utils.print_tp_fp_distribution(tp_fp_distribution_rounded)

    # localization evaluation
    overall_localization_evaluation_data = get_localization_evaluation_data(dp_predictions_segments, dp_expectations_segments, dp_predictions_labels, dp_expectations_labels)
    utils.write_json_file(overall_localization_evaluation_data, "overall_localization_evaluation_data_" + str(score_threshold_value))
    utils.print_write_localization_evaluation_result(overall_localization_evaluation_data, "overall_localization_evaluation_data_" + str(score_threshold_value))

    ########################################
    # for web datapoints
    ########################################
    web_dp_predictions_bin = []
    web_dp_expectations_bin = []
    web_dp_predictions_segments = []
    web_dp_expectations_segments = []
    web_dp_predictions_labels = []
    web_dp_expectations_labels = []
    for i in range(len(types)):
        if types[i] == "web":
            web_dp_predictions_bin.append(dp_predictions_bin[i])
            web_dp_expectations_bin.append(dp_expectations_bin[i])
            web_dp_predictions_segments.append(dp_predictions_segments[i])
            web_dp_expectations_segments.append(dp_expectations_segments[i])
            web_dp_predictions_labels.append(dp_predictions_labels[i])
            web_dp_expectations_labels.append(dp_expectations_labels[i])
    # classification evaluation
    web_classification_evaluation_data = get_classification_evaluation_data(web_dp_predictions_bin, web_dp_expectations_bin)
    utils.write_json_file(web_classification_evaluation_data, "web_classification_evaluation_data_" + str(score_threshold_value))
    utils.print_write_classification_evaluation_result(web_classification_evaluation_data, "web_classification_evaluation_data_" + str(score_threshold_value))

    # aggregate evaluation
    web_classification_evaluation_aggregate_data = get_classification_evaluation_aggregate_data(web_dp_predictions_bin, web_dp_expectations_bin)
    utils.print_classification_evaluation_aggregate_result(web_classification_evaluation_aggregate_data)

    # localization evaluation
    web_localization_evaluation_data = get_localization_evaluation_data(web_dp_predictions_segments, web_dp_expectations_segments, web_dp_predictions_labels, web_dp_expectations_labels)
    utils.write_json_file(web_localization_evaluation_data, "web_localization_evaluation_data_" + str(score_threshold_value))
    utils.print_write_localization_evaluation_result(web_localization_evaluation_data, "web_localization_evaluation_data_" + str(score_threshold_value))

    ########################################
    # for mobile datapoints
    ########################################
    mobile_dp_predictions_bin = []
    mobile_dp_expectations_bin = []
    mobile_dp_predictions_segments = []
    mobile_dp_expectations_segments = []
    mobile_dp_predictions_labels = []
    mobile_dp_expectations_labels = []
    for i in range(len(types)):
        if types[i] == "mobile":
            mobile_dp_predictions_bin.append(dp_predictions_bin[i])
            mobile_dp_expectations_bin.append(dp_expectations_bin[i])
            mobile_dp_predictions_segments.append(dp_predictions_segments[i])
            mobile_dp_expectations_segments.append(dp_expectations_segments[i])
            mobile_dp_predictions_labels.append(dp_predictions_labels[i])
            mobile_dp_expectations_labels.append(dp_expectations_labels[i])
    # classification evaluation
    mobile_classification_evaluation_data = get_classification_evaluation_data(mobile_dp_predictions_bin, mobile_dp_expectations_bin)
    utils.write_json_file(mobile_classification_evaluation_data, "mobile_classification_evaluation_data_" + str(score_threshold_value))
    utils.print_write_classification_evaluation_result(mobile_classification_evaluation_data, "mobile_classification_evaluation_data_" + str(score_threshold_value))

    # aggregate evaluation
    mobile_classification_evaluation_aggregate_data = get_classification_evaluation_aggregate_data(mobile_dp_predictions_bin, mobile_dp_expectations_bin)
    utils.print_classification_evaluation_aggregate_result(mobile_classification_evaluation_aggregate_data)

    # localization evaluation
    mobile_localization_evaluation_data = get_localization_evaluation_data(mobile_dp_predictions_segments, mobile_dp_expectations_segments, mobile_dp_predictions_labels, mobile_dp_expectations_labels)
    utils.write_json_file(mobile_localization_evaluation_data, "mobile_localization_evaluation_data_" + str(score_threshold_value))
    utils.print_write_localization_evaluation_result(mobile_localization_evaluation_data, "mobile_localization_evaluation_data_" + str(score_threshold_value))
