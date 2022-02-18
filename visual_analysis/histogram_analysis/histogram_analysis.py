
import cv2
import glob

import utils

def analyze_histogram(file):
    text_segments_info = []
    f = open(file)

    data = json.load(f)
    for text_segment in data["texts"]:
        # image creation from bbox info
        # to do

        # histogram analysis
        hist = calculate_histogram(file)
        hist_info = get_contrast(hist)

        # populate json
        segment_info = {}
        segment_info["bbox_info"}] = text_segment
        segment_info["hist_info"}] = hist_info
        text_segments_info.append(segment_info)


def calculate_histogram(image):
    img = cv2.imread(image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # compute a grayscale histogram
    hist = cv2.calcHist([img], [0], None, [256], [0, 3])
    # plot the histogram
    utils.plot_histogram(hist)
    return hist

def get_contrast(hist):
    hist /= hist.sum()
    # print(hist[0], hist[85], hist[170])
    return {"bin_info": [hist[0], hist[85], hist[170]], "intensity": None}


files = [file for file in glob.glob("/home/hasan/Downloads/sample_dp_images/data/output/ocr/*.json")]
files.sort()
for file in files:
    print('----------- processing: ', file, '-------------')
    analyze_histogram(file) # later we will input bbox
