import glob
import text_analysis.pattern_matching.matching as pattern_matching
import visual_analysis.histogram_analysis.histogram_analysis as histogram_analysis
import spatial_analysis.proximity_analysis.proximity_analysis as proximity_analysis
import spatial_analysis.size_analysis.size_analysis as size_analysis
import object_detection.object_detection as object_detection
import dp_resolver.resolver as resolver
import evaluation.evaluation as evaluation
from config import *
import utils.utils as utils

import warnings
warnings.filterwarnings('ignore')

# get input image files
img_files = [file for file in glob.glob("UIED/data/input/" + "*.*")]
img_files.sort()
# print(img_files)

# get OCR files
ocr_files = [file for file in glob.glob("UIED/data/output/ocr/" + "*.json")]
ocr_files.sort()
# print(ocr_files)

# predictions, expectations and types
dp_predictions_labels = []
dp_predictions_segments = []
dp_predictions_bin = []

dp_expectations_labels = []
dp_expectations_segments = []
dp_expectations_bin = []

types = []

# threshold value for score
score_threshold_value = .75

# initialize tp fp 2D matrix
# tp_fp_matrix = evaluation.init_tp_fp_matrix()

# iterate over the OCR files
for i in range(len(ocr_files)):
    print(i, ". processing: ", img_files[i])

    # print("------------text_analysis-----------")
    analysis_result = pattern_matching.match_patterns(ocr_files[i])
    # print("------------visual_analysis-----------")
    image_file = img_files[i]
    analysis_result = histogram_analysis.analyze_histogram(analysis_result, image_file)
    # print("------------proximity_analysis-----------")
    analysis_result = proximity_analysis.analyze_proximity(analysis_result, image_file)
    # print("------------size_analysis-----------")
    analysis_result = size_analysis.analyze_size(analysis_result)
    # print("------------object_detection-----------")
    object_detection_result = object_detection.get_object_detection_result(ocr_files[i])

    # print("------------dp resolve-----------")
    input_to_resolver = {"analysis_result": analysis_result, "object_detection_result": object_detection_result}
    dp_predicted = resolver.resolve_dp(input_to_resolver, score_threshold_value)
    dp_predictions_labels.append(dp_predicted["labels"]) # dp_predicted["labels"] is an array of labels
    dp_predictions_bin.append(dp_predicted["labels_binarization"]) # dp_predicted["labels_binarization"] is an array of 0/1 binary values
    dp_predictions_segments.append(dp_predicted["segments"]) # dp_predicted["segments"] is an array of segment objects

    # print("------------dp ground truth-----------")
    dp_ground_truth = evaluation.get_dp_ground_truth(image_file)
    dp_expectations_labels.append(dp_ground_truth["labels"])
    dp_expectations_bin.append(dp_ground_truth["labels_binarization"])
    dp_expectations_segments.append(dp_ground_truth["segments"])
    types.append(dp_ground_truth["type"])

    # print("------------predicted and ground truth labels-----------")
    # print("dp_predicted[labels]", dp_predicted["labels"])
    # print("dp_ground_truth[labels]", dp_ground_truth["labels"])

    # drawing ground truth and predicted bboxes
    # utils.draw_expectation_prediction_bbox(image_file, dp_ground_truth["segments"], dp_predicted["segments"], dp_ground_truth["labels"], dp_predicted["labels"])

    # if(("NO DP" in dp_predicted["labels"])):
    #     # if(image_file == "UIED/data/input/music_30--Music-Bass-Equalizer-0-6_6cef.jpg"):
    #     # print("########################################## filename: ", image_file.split("/")[-1], "####################################")
    #     print("########################################## DEBUG ####################################")
    #     print("dp_ground_truth: ", dp_ground_truth["labels"])
    #     print("dp_predicted: ", dp_predicted["labels"])
    #     # utils.print_dictionary(analysis_result, "analysis_result")
    #     ui_dp = resolver.get_ui_dp(input_to_resolver)
    #     utils.print_dictionary(ui_dp, "ui_dp")
    #     print("########################################## DEBUG ####################################")

    print("----------------------------------------------------------------------------------------------------------------------------------------------")

# evaluation
# tp_fp_matrix = evaluation.set_tp_fp_matrix(dp_predictions_bin, dp_expectations_bin)
# evaluation.print_tp_fp_matrix(tp_fp_matrix)
evaluation.evaluate(dp_predictions_bin, dp_expectations_bin, dp_predictions_segments, dp_expectations_segments, dp_predictions_labels, dp_expectations_labels, types, score_threshold_value)

#####################################################################################################################################################
################################# DEBUGGING #########################################################################################################
#####################################################################################################################################################
# if(image_file.split("/")[-1] == "(159)www.victorianplumbing.co.uk_62cc.jpg"):
#     print("\n####################################  filename: ", image_file.split("/")[-1], "######################################################")
#     print("dp_ground_truth: ", dp_ground_truth["labels"])
#     print("dp_predicted: ", dp_predicted["labels"])
#     utils.print_dictionary(analysis_result, "analysis_result")
#     ui_dp = resolver.get_ui_dp(input_to_resolver)
#     utils.print_dictionary(ui_dp, "ui_dp")
#     break

# if("DEFAULT CHOICE" in dp_predicted["labels"]):
#     # if(image_file == "UIED/data/input/music_30--Music-Bass-Equalizer-0-6_6cef.jpg"):
#     print("########################################## filename: ", image_file.split("/")[-1], "####################################")
#     print("dp_ground_truth: ", dp_ground_truth["labels"])
#     print("dp_predicted: ", dp_predicted["labels"])
#     utils.print_dictionary(analysis_result, "analysis_result")
#     ui_dp = resolver.get_ui_dp(input_to_resolver)
#     utils.print_dictionary(ui_dp, "ui_dp")

# if("NO DP" in dp_ground_truth["labels"]):
#     # if(image_file == "UIED/data/input/music_30--Music-Bass-Equalizer-0-6_6cef.jpg"):
#     # print("########################################## filename: ", image_file.split("/")[-1], "####################################")
#     print("########################################## DEBUG ####################################")
#     print("dp_ground_truth: ", dp_ground_truth["labels"])
#     print("dp_predicted: ", dp_predicted["labels"])
#     # utils.print_dictionary(analysis_result, "analysis_result")
#     ui_dp = resolver.get_ui_dp(input_to_resolver)
#     utils.print_dictionary(ui_dp, "ui_dp")
#     print("########################################## DEBUG ####################################")
