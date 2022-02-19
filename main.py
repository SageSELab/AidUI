import glob
import text_analysis.pattern_matching.matching as pattern_matching

files = [file for file in glob.glob("UIED/data/output/ocr/" + "*.json")]
files.sort()
for file in files:
    print('----------- processing: ', file, '-------------')
    # text analysis (pattern matching)
    pattern_matching.match_patterns(file)
    # visual analysis (histogram analysis)
    # spatial analysis (proximity analysis)
    # spatial analysis (size analysis)
