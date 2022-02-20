import glob
import text_analysis.pattern_matching.matching as pattern_matching
import visual_analysis.histogram_analysis.histogram_analysis as histogram_analysis
import utils.utils as utils

# get input image files
img_files = [file for file in glob.glob("UIED/data/input/" + "*.*")]
img_files.sort()
print(len(img_files))
# get OCR files
ocr_files = [file for file in glob.glob("UIED/data/output/ocr/" + "*.json")]
ocr_files.sort()
print(len(ocr_files))

# iterate over the OCR files
for i in range(len(ocr_files)):
    print('###################### processing: ', ocr_files[i], '######################')
    print("------------text_analysis_output-----------")
    dictionary_text_analysis = pattern_matching.match_patterns(ocr_files[i])
    utils.print_dictionary(dictionary_text_analysis)
    print("------------visual_analysis_output-----------")
    image_file = img_files[i]
    dictionary_visual_analysis = histogram_analysis.analyze_histogram(dictionary_text_analysis, image_file)
    utils.print_dictionary(dictionary_visual_analysis)
    # utils.print_dictionary(dictionary_visual_analysis)
    print("------------proximity_analysis_output-----------")
    print("------------size_analysis_output-----------")
