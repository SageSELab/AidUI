
import cv2
import glob

import utils

def analyze_histogram(file):
    #segments go to get_histogram function
    hist = get_histogram(file)
    get_contrast(hist)

def get_histogram(image):
    img = cv2.imread(image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # compute a grayscale histogram
    hist = cv2.calcHist([img], [0], None, [256], [0, 4])
    # plot the histogram
    utils.plot_histogram(hist)
    return hist

def get_contrast(hist):
    # return json with bbox & classification
    print(hist.sum())
    print(hist[0], hist[64], hist[128], hist[192])
    pass


files = [file for file in glob.glob("/home/hasan/Downloads/sample_dp_images/*")]
files.sort()
for file in files:
    print('----------- processing: ', file, '-------------')
    analyze_histogram(file) # later we will input bbox
