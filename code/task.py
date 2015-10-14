from __future__ import division
__author__ = 'Louis'

import os
import scipy.cluster.hierarchy as hier
from sklearn.metrics.pairwise import cosine_distances
from html_handle import handle_html
from html_handle import pre_process

def printout(name, arr):
    header = '<?xml version="1.0" encoding="UTF-8"?>\n<clustering name="' + name + '">"\n'
    footer = '</clustering>\n'
    out = open(output_test+ "/" + name + ".clust.xml", 'w')
    out.write(header)
    for i in range(len(arr)):
        out.write('\t<entity id="' + str(i) + '">\n')
        for j in range(len(arr[i])):
            out.write('\t\t<doc rank="' + str(arr[i][j]) + '" />\n')
        out.write('\t</entity>\n')
    out.write(footer)
    out.close()
    #print("writing end")

def sortClusters(arr):
    output = []

    for i in range(max(arr)):
        output.append([])
        for j in range(len(arr)):
            if i+1 == arr[j]:
                output[i].append(j)

    return output

input_dir = "../training"
input_test = "../test"
output_test = "../output"

"""
for name in os.listdir(input_dir):
    streng = input_dir + "/" + name + "/docs"
    vocabulary = []
    print(name)
    for site in os.listdir(streng):
        nyStreng = input_dir + "/" + name + "/docs/" + site
        voc = handle_html(nyStreng)
        vocabulary.append(voc)
    try:
        matrix = pre_process(vocabulary)
    except ValueError:
        print(name + " failed to read")

    dist = cosine_distances(matrix)
    link = hier.linkage(dist, method="average")
    clust = hier.fcluster(link, t=0.1)
    #print(clust)


"""
print("starting predictions")
for name in os.listdir(input_test):
    streng = input_test + "/" + name + "/docs"
    vocabulary = []
    #print(name)
    for site in os.listdir(streng):
        nyStreng = input_test + "/" + name + "/docs/" + site
        voc = handle_html(nyStreng)
        vocabulary.append(voc)
    try:
        matrix = pre_process(vocabulary)
    except ValueError:
        print(name + " failed to predict")

    dist = cosine_distances(matrix)
    link = hier.linkage(dist, method="centroid", metric="euclidean")
    clust = hier.fcluster(link, t=0.08)
    d = sortClusters(clust)
    printout(name,d)
    #print(pred)

print("done")