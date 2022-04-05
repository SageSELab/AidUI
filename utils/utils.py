import cv2
import json
from matplotlib import pyplot as plt
import pandas as pd

import pprint
pp = pprint.PrettyPrinter()

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

def print_write_dict_as_panda_table(dict, title):
    num_total_dp_instances = dict["num_total_dp_instances"]
    accuracy = dict["accuracy"]
    weighted_avg_precision = dict["weighted_avg_precision"]
    weighted_avg_recall = dict["weighted_avg_recall"]
    macro_avg_precision = dict["macro_avg_precision"]
    macro_avg_recall = dict["macro_avg_recall"]
    aggregate_rows = [[
        num_total_dp_instances
        , accuracy
        , weighted_avg_precision
        , weighted_avg_recall
        , macro_avg_precision
        , macro_avg_recall
    ]]

    category_rows = []
    for category, values in dict["category_info"].items():
        row = []
        row.append(category)
        row.append(values["num_instances"])
        row.append(values["precision"])
        row.append(values["recall"])
        category_rows.append(row)

    # panda dataframes
    aggregate_results = pd.DataFrame(aggregate_rows, columns=["num_total_dp_instances", "accuracy", "weighted_avg_precision", "weighted_avg_recall", "macro_avg_precision", "macro_avg_recall"])
    category_results = pd.DataFrame(category_rows, columns=["category", "num_instances", "precision", "recall"])

    # print in table
    print("\n----------------------------", title, "----------------------------")
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
    aggregate_rows = [[avg_iou]]

    category_rows = []
    for category, values in dict["dp_iou_info"].items():
        row = []
        row.append(category)
        row.append(values["avg_iou"])
        category_rows.append(row)

    # panda dataframes
    aggregate_results = pd.DataFrame(aggregate_rows, columns=["avg_iou"])
    category_results = pd.DataFrame(category_rows, columns=["category", "avg_iou"])

    # print in table
    print("\n----------------------------", title, "----------------------------")
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
