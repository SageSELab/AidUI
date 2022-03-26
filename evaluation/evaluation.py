# https://towardsdatascience.com/evaluating-multi-label-classifiers-a31be83da6ea
import json
import shutil
import numpy as np
from sklearn.metrics import multilabel_confusion_matrix
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
    ground_truth = None
    for filename in data.keys():
        if filename == img_filename:
            ground_truth = data[filename]
    # label binarization
    dps = ground_truth["labels"]
    print(dps)
    dp_ground_truth = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if len(dps) != 0:
        for dp in dps:
            index = class_dp_bin_index[dp]
            dp_ground_truth[index] = 1
    print(dp_ground_truth)
    return dp_ground_truth

def test_confusion_matrix():
    y_gt = np.array([[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    y_predicted = np.array([[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    confusion_matrix = multilabel_confusion_matrix(y_gt, y_predicted)
    # print(confusion_matrix)
    # print(len(confusion_matrix))
    print(confusion_matrix[5])
    print(confusion_matrix[6])
