from __future__ import division
__author__ = 'Louis'

import os
import numpy as np
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import AgglomerativeClustering
from collections import defaultdict

input_dir = "../training"



d = defaultdict(list)
i = 0
#print("Line")
for name in os.listdir(input_dir):
    #print(name)
    streng = input_dir + "/" + name + "/docs"
    #print(streng)

    for site in os.listdir(streng):
        #print(name + ": " + i)
        #synopsis[].append(site)
        d[name].append(site)
        #name.append(i)
        #print(name[j])
    i += 1
    #print(j)
    #print(name[40])

print(d("Abby_Watkins"))
#print(Abby_Watkins)