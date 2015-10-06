from __future__ import division
from html.parser import HTMLParser
import csv


class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.vocabulary = []

    def get_vocabulary(self):
        return self.vocabulary

    def handle_data(self, data):
        data_words = data.split()
        if len(data_words) >= 10:
            for i in range(len(data_words)):
                self.vocabulary.append(data_words[i])




def handle_html(path):
    file = open(path)
    html = file.read()
    parser = MyHTMLParser()
    parser.feed(html)
    return parser.get_vocabulary()

print (handle_html("001.html"))

