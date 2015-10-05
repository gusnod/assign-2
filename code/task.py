from __future__ import division
__author__ = 'Louis'

import numpy as np
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import AgglomerativeClustering
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        vocabulary = []
        if len(data) >= 10:
            vocabulary.append(data)
            print(data)
        return vocabulary

parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me because i am looong enough to be parsed, yaay!</h1><p>do not</body></html>')
