import os
import re
import MeCab
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer

mecab = MeCab.Tagger()
mecab.parse("")


def tf(doc):
    #vectorizer = CountVectorizer(token_pattern=u'(?u)\\b\\w+\\b')
    vectorizer = TfidfVectorizer(
        min_df=1, max_df=50, token_pattern=u'(?u)\\b\\w+\\b')
    features = vectorizer.fit_transform(doc)
    #terms = vectorizer.get_feature_names()
    # return features, terms
    feature_array = np.array(vectorizer.get_feature_names())
    tfidf_sorting = np.argsort(features.toarray()).flatten()[::-1]
    topn = feature_array[tfidf_sorting][:10]
    return topn, tfidf_sorting[:10]


def tfidf(docs):
    vectorizer = TfidfVectorizer(
        min_df=1, max_df=50, token_pattern=u'(?u)\\b\\w+\\b')
    features = vectorizer.fit_transform(docs)
    terms = vectorizer.get_feature_names()
    return features, terms


def wakati(line):

    global w
    global docs

    node = mecab.parseToNode(line)
    while node:
        feature = node.feature.split(",")

        # 除外/包含リスト
        if (not feature[2] == "人名") and ((re.search('[0-9０-９]+', node.surface) and feature[6] == "*") or (not feature[6] == "*")):
            if feature[0] == "名詞":
                w += node.surface
            else:
                if w:
                    wL.append(w)
                w = ""
        node = node.next
path = os.getcwd() + "/data/"
files = []
texts = []
docs = []
for x in os.listdir(path):
    if os.path.isfile(path + x):
        files.append(x)

for file in files:
    if(file[-4:] == '.txt'):

        w = ""
        wL = []
        f = open(path + file, 'r', encoding='shift-jis')
        for line in f:
            line = re.sub('¥s|　|¥n|¥r', '', line)
            wakati(line)
        docs.append(wL)
        #print (docs)
docs = [' '.join(d) for d in docs]

res = tf(docs)
print(res)

'''
features, terms = tf(docs)
print(terms)
print(features)

print ("--")

features, terms = tfidf(docs)
print(terms)
print(features.toarray())
'''
