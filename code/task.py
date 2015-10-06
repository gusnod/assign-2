from __future__ import division
__author__ = 'Louis'

import numpy as np
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import AgglomerativeClustering


class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.vocabulary = []

    def get_vocabulary(self):
        return self.vocabulary

    def handle_data(self, data):
        data_words = data.split()
        if len(data_words) >= 10:
            print(data_words)
            for i in range(len(data_words)):
                self.vocabulary.append(data_words[i])

parser = MyHTMLParser()
html = ('<html><head><title>Test</title></head>'
        '<body><h1>Parse me because i am looong enough to be parsed, yaay!</h1><p>do not whohoho sdasdfg</p><p>And'
        'I will be longer than 10 words because we need to test that the vocabulary actually works</p></body></html>')
parser.feed(html)
print("Vocabulary")
print(parser.get_vocabulary())
