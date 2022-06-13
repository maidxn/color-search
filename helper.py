import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
import pickle


def CalHistogram(image_path, bin=[8, 8, 8]):
    if os.path.exists(image_path):
        img = cv.imread(image_path)
    else:
        img = image_path
    img = img[:,:,:3]
    hist = cv.calcHist([img], [0, 1, 2], None, [bin[0], bin[1], bin[2]], [0,256, 0, 256, 0, 256])
    hist = hist.reshape(1, -1)/hist.sum()
    return hist


def CalculateCosine_Holiday(query_path, data_feature, bin=[8, 8, 8]):
    query_feature = CalHistogram(query_path, bin)
    cosine_array = [cosine_similarity(query_feature, i.reshape(1, -1)) for i in data_feature]
    res = [cosine_array[i][0][0] for i in range(len(data_feature))]
    res = np.array(res)
    return res
