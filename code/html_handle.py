from __future__ import division
from html.parser import HTMLParser
from sklearn.feature_extraction.text import CountVectorizer
import lxml
from lxml.html.clean import Cleaner


class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.vocabulary = []
        self.current_tag = 0

    def get_vocabulary(self):
        return self.vocabulary

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag

    def handle_data(self, data):
        if self.current_tag != "script" and self.current_tag != "style":
            data_words = data.split()
            #if len(data_words) >= 10:
            for i in range(len(data_words)):
                self.vocabulary.append(data_words[i])


def pre_process(vocabulary):
    cv = CountVectorizer(stop_words="english")
    cv.fit_transform(vocabulary)
    cv.strip_accents = True
    cv.lowercase = True

    return cv.vocabulary_

def handle_html(path):
    file = open(path)
    html = file.read()
    #print(html)
    parser = MyHTMLParser()
    parser.feed(html)
    vocabulary = parser.get_vocabulary()
    word_list = pre_process(vocabulary)
    return word_list

print(handle_html("001.html"))

