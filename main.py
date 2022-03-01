import glob
import text_analysis.pattern_matching.matching as pattern_matching
import visual_analysis.histogram_analysis.histogram_analysis as histogram_analysis
import spatial_analysis.proximity_analysis.proximity_analysis as proximity_analysis
import spatial_analysis.size_analysis.size_analysis as size_analysis
import object_detection.object_detection as object_detection
import dp_resolver.resolver as resolver
import utils.utils as utils

# get input image files
img_files = [file for file in glob.glob("UIED/data/input/" + "*.*")]
img_files.sort()
# print(len(img_files))

# get OCR files
ocr_files = [file for file in glob.glob("UIED/data/output/ocr/" + "*.json")]
ocr_files.sort()
# print(len(ocr_files))

# iterate over the OCR files
for i in range(len(ocr_files)):
    print('###################### processing: ', ocr_files[i], '######################')

    # print("------------text_analysis-----------")
    analysis_result = pattern_matching.match_patterns(ocr_files[i])
    # print("------------visual_analysis-----------")
    image_file = img_files[i]
    analysis_result = histogram_analysis.analyze_histogram(analysis_result, image_file)
    # # print("------------proximity_analysis-----------")
    analysis_result = proximity_analysis.analyze_proximity(analysis_result, image_file)
    # print("------------size_analysis-----------")
    analysis_result = size_analysis.analyze_size(analysis_result)

    # # print analysis result
    # utils.print_dictionary(analysis_result)
    # # write analysis result
    # utils.write_json_file(analysis_result)

    # print("------------object_detection-----------")
    object_detection_result = object_detection.get_object_detection_result()

    # print("------------dp_resolver-----------")
    input_to_resolver = {"analysis_result": analysis_result, "object_detection_result": object_detection_result}
    ui_dp = resolver.resolve_dp(input_to_resolver)
    utils.print_dictionary(ui_dp)
