"""
Most of this code is based on my previous code for getting the webcam to recognize an object which is based on the following tutorials:
    https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
    https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html

The k-means clustering was based on the following explanation for k-means clustering:
    https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097

I combined the code together so that instead of reading from a specific image for k-means clustering, it read from the webcam. In addition I made sure the webcam was updating so it didn't just read a static image but instead got a constant feed frm the webcam.
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist
def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar

cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()

    cv.imshow('frame',frame)

    #img = cv.imread("pic/img7.jpeg")
    img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    img = img.reshape((img.shape[0] * img.shape[1],3)) #represent as row*column,channel number
    clt = KMeans(n_clusters=3) #cluster number
    clt.fit(img)

    hist = find_histogram(clt)
    bar = plot_colors2(hist, clt.cluster_centers_)

    plt.close()
    plt.axis("off")
    plt.imshow(bar)
    plt.show(block=False)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()