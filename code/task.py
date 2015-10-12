from __future__ import division
__author__ = 'Louis'

import os
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.pairwise import cosine_similarity
from html_handle import handle_html
from html_handle import pre_process
from xml.dom import minidom
from nltk.stem.snowball import SnowballStemmer
import nltk
import re

stemmer = SnowballStemmer("english")

def baseline(name, labels):
    xmldoc = minidom.parse(input_dir + "/" + name + "/" + name + ".xml")
    itemlist = xmldoc.getElementsByTagName("corpus")
    person_name = itemlist[0].attributes['search_string'].value
    header = '<?xml version="1.0" encoding="UTF-8"?>\n<clustering name="' + person_name + '">"\n'
    footer = '</clustering>\n'

    itemlist = xmldoc.getElementsByTagName('doc')
    docs = [s.attributes['rank'].value for s in itemlist]

    out_oio = open(output_test+ "/" + name + ".clust.xml", 'w')
    out_oio.write(header)
    for idx in enumerate(labels): #TODO find a test to see how many clusters there is
        out_oio.write('\t<entity id="' + str(idx) + '">\n')
        for d in labels[idx]: #TODO find a test to see how many entries in that cluster
            out_oio.write('\t\t<doc rank="' + d + '" />\n')
        out_oio.write('\t</entity>\n')
    out_oio.write(footer)
    out_oio.close()

input_dir = "../training"
input_test = "../test"
output_test = "../output"

#d = defaultdict(list)

ag = AgglomerativeClustering(compute_full_tree="auto", linkage= "complete")
for name in os.listdir(input_dir):
    streng = input_dir + "/" + name + "/docs"
    vocabulary = []
    #print(name)
    for site in os.listdir(streng):
        nyStreng = input_dir + "/" + name + "/docs/" + site
        if os.path.getsize(nyStreng) > 400:
            voc = handle_html(nyStreng)
            vocabulary.append(voc)
            #d[name].append(voc)
    try:
        matrix = pre_process(vocabulary)
    except ValueError:
        print("oops")

    dist = 1 - cosine_similarity(matrix)
    ag.fit(dist)
    #print("fitted")

print("starting predictions")
for name in os.listdir(input_test):
    streng = input_test + "/" + name + "/docs"
    vocabulary = []
    print(name)
    for site in os.listdir(streng):
        nyStreng = input_test + "/" + name + "/docs/" + site
        if os.path.getsize(nyStreng) > 400:
            voc = handle_html(nyStreng)
            vocabulary.append(voc)

    try:
        matrix = pre_process(vocabulary)
    except ValueError:
        print("oops")

    dist = 1 - cosine_similarity(matrix)
    pred = ag.fit_predict(dist)
    print(pred)


print("done")

