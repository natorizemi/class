from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import copy


class Analysis():
    def __init__(self):
        pass

    def analyze(self, filenames):
        # max_dfは0.5（半分以上の文書に出現する言葉はいらん）を設定
        count_vectorizer = CountVectorizer(
            input='filename', max_df=0.5, min_df=1, max_features=3000,
            encoding="shift_jis"
        )
        # 引数として、CountVectorizerとTfidfTransformerで使った双方の引数が指定できるようになっている
        tfidf_vectorizer = TfidfVectorizer(
            input='filename', max_df=0.5, min_df=1, max_features=3000,
            norm='l2', encoding="shift_jis"
        )

        tf = count_vectorizer.fit_transform(docs)
        features = count_vectorizer.get_feature_names()

        tfidf = tfidf_vectorizer.fit_transform(docs)
        print(tfidf)

        print("--")
        for j in ['老人', '政治']:
            word_result = tfidf.toarray()[:, features.index(j)]
            word2_result = copy.deepcopy(word_result)
            word_list = word_result.tolist()
            test = sorted(word2_result, reverse=True)
            positions = []
            for j in test[:10]:
                positions.append(word_list.index(j))

            print(positions)
