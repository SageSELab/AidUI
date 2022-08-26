import os
import cv2
import json
from matplotlib import pyplot as plt
import pandas as pd
from config import *

import pprint
pp = pprint.PrettyPrinter()

def print_array(array):
    pp.pprint(array)

def write_json_file(dict, filename):
    file = "./output/" + filename + ".json"
    with open(file, 'w') as fp:
        json.dump(dict, fp)

def print_dictionary(dictionary, title):
    print("\n----------------------------", title, "----------------------------")
    pp.pprint(dictionary)

def show_image(img):
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def plot_histogram(hist):
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()

def plot_barchart():
    # freq per category
    category_frequencies = []
    for i in range(16):
        category_frequencies.append(i)
    categories = []
    for i in range(16):
        categories.append(i)

    # plot bar chart
    plt.bar(categories, category_frequencies)
    plt.tick_params(labelsize=10)
    plt.xticks(rotation=70)
    # plt.show()
    plt.savefig('books_read.png')

def print_tp_fp_distribution(tp_fp_distribution_rounded):
    category_rows = []
    for i in range(len(tp_fp_distribution_rounded)):
        # print(class_bin_index_to_dp[str(i)])
        # print(tp_fp_distribution_rounded[i])
        row = []
        category = class_bin_index_to_dp[str(i)]
        # category_row = tp_fp_distribution_rounded[i]
        if(category not in classes_excluded_in_report):
            row.append(category)
            category_row = tp_fp_distribution_rounded[i]
            for j in range(len(category_row)):
                category_acronym = class_bin_index_to_dp_acronym[str(j)]
                if(category_acronym not in classes_acronyms_excluded_in_report):
                    row.append(category_row[j])
            category_rows.append(row)

    category_columns = []
    category_columns.append("category")
    for i in range(len(tp_fp_distribution_rounded)):
        category_acronym = class_bin_index_to_dp_acronym[str(i)]
        if(category_acronym not in classes_acronyms_excluded_in_report):
            category_columns.append(category_acronym)

    # panda dataframes
    results = pd.DataFrame(category_rows, columns=category_columns)
    print("::::::::::::::::::::TP FP Distribution Results::::::::::::::::::::")
    print(results)

def print_classification_evaluation_aggregate_result(dict):
    aggregate_rows = []
    for category, values in dict.items():
        row = []
        row.append(category)
        row.append(values["num_data_points"])
        row.append(values["num_instances"])
        row.append(values["num_fp"])
        row.append(values["precision"])
        row.append(values["recall"])
        row.append(values["f1score"])
        aggregate_rows.append(row)

    # panda dataframes
    aggregate_results = pd.DataFrame(aggregate_rows, columns=["category", "num_data_points", "num_instances", "num_fp", "precision", "recall", "f1score"])

    # print in table
    print("::::::::::::::::::::Aggregate Results::::::::::::::::::::")
    print(aggregate_results)

def print_write_classification_evaluation_result(dict, title):
    num_data_points = dict["num_data_points"]
    num_total_dp_instances = dict["num_total_dp_instances"]
    accuracy = dict["accuracy"]
    weighted_avg_precision = dict["weighted_avg_precision"]
    weighted_avg_recall = dict["weighted_avg_recall"]
    macro_avg_precision = dict["macro_avg_precision"]
    macro_avg_recall = dict["macro_avg_recall"]
    avg_precision = dict["avg_precision"]
    avg_recall = dict["avg_recall"]
    avg_f1score = dict["avg_f1score"]
    aggregate_rows = [[
        num_data_points
        , num_total_dp_instances
        , accuracy
        , weighted_avg_precision
        , weighted_avg_recall
        , macro_avg_precision
        , macro_avg_recall
        , avg_precision
        , avg_recall
        , avg_f1score
    ]]

    category_rows = []
    for category, values in dict["category_info"].items():
        if(category not in classes_excluded_in_report):
            row = []
            row.append(category)
            row.append(values["num_instances"])
            row.append(values["precision"])
            row.append(values["recall"])
            row.append(values["f1score"])
            category_rows.append(row)

    # panda dataframes
    aggregate_results = pd.DataFrame(aggregate_rows, columns=["num_data_points", "num_total_dp_instances", "accuracy", "weighted_avg_precision", "weighted_avg_recall", "macro_avg_precision", "macro_avg_recall", "avg_precision", "avg_recall", "avg_f1score"])
    category_results = pd.DataFrame(category_rows, columns=["category", "num_instances", "precision", "recall", "f1score"])

    # print in table
    print("\n###############################################################################################################################")
    print("\n##########################################################", title, "#######################")
    print("\n###############################################################################################################################")
    print("\n::::::::::::::::::::Aggregate Results::::::::::::::::::::")
    print(aggregate_results)
    print("\n::::::::::::::::::::::Category Results:::::::::::::::::::")
    print(category_results)

    # write tables in file
    filename = "./output/" + title + ".txt"
    f = open(filename, "w")
    print("\n::::::::::::::::::::Aggregate Results::::::::::::::::::::\n"
    , aggregate_results
    , "\n::::::::::::::::::::::Category Results:::::::::::::::::::\n"
    , category_results, file=f)
    # print(aggregate_results, file=f)
    # print("\n::::::::::::::::::::::Category Results:::::::::::::::::::")
    # print(category_results, file=f)
    f.close()

def print_write_localization_evaluation_result(dict, title):
    avg_iou = dict["avg_iou"]
    # do for custom
    custom_avg_iou = dict["custom_avg_iou"]
    aggregate_rows = [[avg_iou, custom_avg_iou]]

    category_rows = []
    for category, values in dict["dp_iou_info"].items():
        row = []
        row.append(category)
        row.append(values["avg_iou"])
        row.append(values["custom_avg_iou"])
        category_rows.append(row)

    # panda dataframes
    aggregate_results = pd.DataFrame(aggregate_rows, columns=["avg_iou", "custom_avg_iou"])
    category_results = pd.DataFrame(category_rows, columns=["category", "avg_iou", "custom_avg_iou"])

    # print in table
    print("\n###############################################################################################################################")
    print("\n##########################################################", title, "#######################")
    print("\n###############################################################################################################################")
    print("\n::::::::::::::::::::Aggregate Results::::::::::::::::::::")
    print(aggregate_results)
    print("\n::::::::::::::::::::::Category Results:::::::::::::::::::")
    print(category_results)

    # write tables in file
    filename = "./output/" + title + ".txt"
    f = open(filename, "w")
    print("\n::::::::::::::::::::Aggregate Results::::::::::::::::::::\n"
    , aggregate_results
    , "\n::::::::::::::::::::::Category Results:::::::::::::::::::\n"
    , category_results, file=f)
    # print(aggregate_results, file=f)
    # print("\n::::::::::::::::::::::Category Results:::::::::::::::::::")
    # print(category_results, file=f)
    f.close()

def draw_expectation_prediction_bbox(file, expected_segments, predicted_segments, expected_labels, predicted_labels):
    if(len(expected_segments) == 1 and len(predicted_segments) == 1):
        if("GAMIFICATION" in expected_labels):
            print("file", file)
            print("---------expected_segments-----------")
            pp.pprint(expected_segments)
            print("---------predicted_segments-----------")
            pp.pprint(predicted_segments)
            try:
                # read the input image
                out_img = cv2.imread(file)
                # draw bounding box
                cv2.rectangle(out_img,(expected_segments[0]["column_min"], expected_segments[0]["row_min"]),(expected_segments[0]["column_max"], expected_segments[0]["row_max"]),(0,255,0), 2)
                cv2.rectangle(out_img,(predicted_segments[0]["column_min"], predicted_segments[0]["row_min"]),(predicted_segments[0]["column_max"], predicted_segments[0]["row_max"]),(0,0,255), 2)
                # write updated image
                destination_dir = "./output/bboxes/"
                filename = file.split("/")[-1]
                if(not os.path.exists(destination_dir)):
                    os.mkdir(destination_dir)
                cv2.imwrite(destination_dir + filename, out_img)
            except Exception as e:
                print(e)
