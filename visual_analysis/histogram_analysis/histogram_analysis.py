from matplotlib import pyplot as plt
import cv2
import glob

def get_histogram(image):
    img = cv2.imread(image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # compute a grayscale histogram
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    # print(len(hist))

    # plot the histogram
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()

files = [file for file in glob.glob("sample_dp_images/*")]
files.sort()
for file in files:
    print('----------- processing: ', file, '-------------')
    get_histogram(file)
