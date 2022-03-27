import cv2
import glob
import utils.utils as utils

def calculate_histogram(image, coordinates):
    # utils.show_image(image)
    img = image[coordinates[0]:coordinates[1], coordinates[2]:coordinates[3]]
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # utils.show_image(img)
    hist = cv2.calcHist([img], [0], None, [2], [0, 256]) # compute a grayscale histogram
    # print(hist)
    # utils.plot_histogram(hist) # plot the histogram
    return hist

def get_opacity(hist):
    opacity = None
    hist /= hist.sum()
    # print(hist[0][0])
    # print(hist[1][0])
    if hist[0][0] > .65:
        opacity = "darker"
    elif hist[1][0] > .65:
        opacity = "brighter"
    else:
        opacity = "normal"
    return opacity

def analyze_histogram(dictionary, image_file):
    img = cv2.imread(image_file)

    # image row/column min/max
    img_row_min = 0
    img_row_max = img.shape[0] - 1
    img_column_min = 0
    img_column_max = img.shape[1] - 1
    img_coordinates = [img_row_min, img_row_max, img_column_min, img_column_max]

    for key, value in dictionary.items():
        coordinates = [
            max(value["segment_info"]["row_min"] - 25, img_coordinates[0]) # max(value["segment_info"]["row_min"] - k, img_coordinates[0])
            , min(value["segment_info"]["row_max"] + 25, img_coordinates[1]) # min(value["segment_info"]["row_max"] + k, img_coordinates[1])
            , max(value["segment_info"]["column_min"] - 50, img_coordinates[2]) # max(value["segment_info"]["column_min"] - k, img_coordinates[2])
            , min(value["segment_info"]["column_max"] + 50, img_coordinates[3]) # min(value["segment_info"]["column_max"] + k, img_coordinates[3])
        ]
        hist = calculate_histogram(img, coordinates)
        opacity = get_opacity(hist)
        visual_analysis = {"hist": [str(hist[0][0]), str(hist[1][0])], "opacity": opacity}
        value["visual_analysis"] = visual_analysis
    return dictionary
