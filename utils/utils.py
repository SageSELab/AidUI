import cv2
import json
from matplotlib import pyplot as plt

import pprint
pp = pprint.PrettyPrinter()

def write_json_file(dict):
    with open('analysis_result.json', 'w') as fp:
        json.dump(dict, fp)

def print_dictionary(dictionary):
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
