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

# get input image files
img_files = [file for file in glob.glob("UIED/data/input/" + "*.*")]
img_files.sort()
# print(img_files)

# get OCR files
ocr_files = [file for file in glob.glob("UIED/data/output/ocr/" + "*.json")]
ocr_files.sort()
# print(ocr_files)

# predictions, expectations and types
dp_predictions = []
dp_expectations = []
types = []

# iterate over the OCR files
for i in range(len(ocr_files)):
    # print('###################### processing: ', ocr_files[i], '######################')

    # print("------------text_analysis-----------")
    analysis_result = pattern_matching.match_patterns(ocr_files[i])
    # print("------------visual_analysis-----------")
    image_file = img_files[i]
    print("###### filename: ", image_file.split("/")[-1])
    analysis_result = histogram_analysis.analyze_histogram(analysis_result, image_file)
    # print("------------proximity_analysis-----------")
    analysis_result = proximity_analysis.analyze_proximity(analysis_result, image_file)
    # print("------------size_analysis-----------")
    analysis_result = size_analysis.analyze_size(analysis_result)
    # print("------------object_detection-----------")
    object_detection_result = object_detection.get_object_detection_result(ocr_files[i])
    # utils.print_dictionary(object_detection_result, "object_detection_result")

    print("------------dp resolver output-----------")
    input_to_resolver = {"analysis_result": analysis_result, "object_detection_result": object_detection_result}
    dp_predicted = resolver.resolve_dp(input_to_resolver)
    dp_predictions.append(dp_predicted)

    print("--------dp ground truth output-----------")
    dp_ground_truth = evaluation.get_dp_ground_truth(image_file)
    dp_expectations.append(dp_ground_truth["labels_binarization"])
    types.append(dp_ground_truth["type"])

# print("######################input for confusion matrix calculation######################")
# print("dp_predictions", dp_predictions)
# print("dp_expectations", dp_expectations)
# print("types", types)

print("######################output of confusion matrix calculation######################")
evaluation.get_evaluation_data(dp_predictions, dp_expectations, types)
