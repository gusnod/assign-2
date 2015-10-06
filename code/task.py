from __future__ import division
__author__ = 'Louis'

import os
import numpy as np
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import AgglomerativeClustering

input_dir = "../training"


#print("Line")
for name in os.listdir(input_dir):
    #print(name)
    streng = input_dir + "/" + name + "/docs"
    #print(streng)
    #name = []
    j = -1
    for i in os.listdir(streng):
        print(name + ": " + i)
        j += 1
        #name.append(i)
        #print(name[j])

    #print(j)
    #print(name[40])

#print(Abby_Watkins)