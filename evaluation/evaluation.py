# https://towardsdatascience.com/evaluating-multi-label-classifiers-a31be83da6ea
import json
import shutil
import numpy as np
from sklearn.metrics import multilabel_confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
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
        for annotation in data["annotations"]:
            if(annotation["image_id"] == img_id):
                category_id = annotation["category_id"]
                for category in data["categories"]:
                    if(category["id"] == category_id):
                        labels.append(category["name"])
        # print(img_filename)
        # print("mobile")
        # print(labels)
        ground_truth_info[img_filename] = {"type": type, "labels": labels}
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
    labels_binarization = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if len(dps) != 0:
        for dp in dps:
            index = class_dp_bin_index[dp]
            labels_binarization[index] = 1
    # print(labels_binarization)
    dp_ground_truth["labels_binarization"] = labels_binarization
    return dp_ground_truth

def get_classification_evaluation_data(dp_predictions, dp_expectations):
    # calculate num of instances, confusion matrix, precision, recall for all dp categories
    num_data_points = len(dp_expectations)
    num_dp_instances = np.array(dp_expectations).sum(0)
    conf_mat = multilabel_confusion_matrix(np.array(dp_expectations), np.array(dp_predictions))
    accuracy = accuracy_score(dp_expectations, dp_predictions)
    precision = precision_score(dp_expectations, dp_predictions, average=None)
    recall = recall_score(dp_expectations, dp_predictions, average=None)

    # populate category_info
    category_info = {}
    for i in range(len(conf_mat)):
        category_info[class_bin_index_to_dp[str(i)]] = {
        "num_instances": str(num_dp_instances[i])
        , "conf_mat": conf_mat[i].tolist()
        , "precision": str(precision[i])
        , "recall": str(recall[i])
    }

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
    return evaluation_data

def evaluate(dp_predictions, dp_expectations, types, score_threshold_value):
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

    # for all datapoints
    overall_classification_evaluation_data = get_classification_evaluation_data(dp_predictions, dp_expectations)
    # utils.print_dictionary(overall_classification_evaluation_data, "overall_classification_evaluation_data")
    utils.write_json_file(overall_classification_evaluation_data, "overall_classification_evaluation_data_" + str(score_threshold_value))
    utils.print_write_dict_as_panda_table(overall_classification_evaluation_data, "overall_classification_evaluation_data_" + str(score_threshold_value))

    # for web datapoints
    web_dp_predictions = []
    web_dp_expectations = []
    for i in range(len(types)):
        if types[i] == "web":
            web_dp_predictions.append(dp_predictions[i])
            web_dp_expectations.append(dp_expectations[i])
    web_classification_evaluation_data = get_classification_evaluation_data(web_dp_predictions, web_dp_expectations)
    # utils.print_dictionary(web_classification_evaluation_data, "web_classification_evaluation_data")
    utils.write_json_file(web_classification_evaluation_data, "web_classification_evaluation_data_" + str(score_threshold_value))
    utils.print_write_dict_as_panda_table(web_classification_evaluation_data, "web_classification_evaluation_data_" + str(score_threshold_value))

    # for mobile datapoints
    mobile_dp_predictions = []
    mobile_dp_expectations = []
    for i in range(len(types)):
        if types[i] == "mobile":
            mobile_dp_predictions.append(dp_predictions[i])
            mobile_dp_expectations.append(dp_expectations[i])
    mobile_classification_evaluation_data = get_classification_evaluation_data(mobile_dp_predictions, mobile_dp_expectations)
    # utils.print_dictionary(mobile_classification_evaluation_data, "mobile_classification_evaluation_data")
    utils.write_json_file(mobile_classification_evaluation_data, "mobile_classification_evaluation_data_" + str(score_threshold_value))
    utils.print_write_dict_as_panda_table(mobile_classification_evaluation_data, "mobile_classification_evaluation_data_" + str(score_threshold_value))
