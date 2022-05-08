import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import pickle


def ConvertRGBToDecimal(triplet):
    R = int(round(triplet[0], 0))
    G = int(round(triplet[1], 0))
    B = int(round(triplet[2], 0))
    return R * 65536 + G * 256 + B


def KMeansExtract(img, number_of_colors=5):
    nrow, ncol, nchl = img.shape
    g = img.reshape(nrow*ncol,nchl)
    clf = KMeans(n_clusters = number_of_colors, random_state = 0)
    k_means = clf.fit(g)
    colors = []
    for each in clf.cluster_centers_:
        color = ConvertRGBToDecimal(each)
        colors.append(color)
    res = np.array(colors).reshape(1, -1)
    return res


def ExtractColors(image_path, number_of_colors=5):
    res = KMeansExtract(image_path, number_of_colors)
    return res


def CalculateCosine(query_path, data_feature, option=0, number_of_colors=5):
    query_feature = ExtractColors(query_path)
    cosine_array = [cosine_similarity(query_feature, i.reshape(1, -1)) for i in data_feature]
    res = [cosine_array[i][0][0] for i in range(len(data_feature))]
    res = np.array(res)
    return res



