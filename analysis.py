from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from numpy import *
import os
import copy

class Analysis():
    def __init__(self):
        pass

    def main(self):
        # 引数として、CountVectorizerとTfidfTransformerで使った双方の引数が指定できるようになっている
        tfidf_vectorizer = TfidfVectorizer(
            input='filename', max_df=0.5, min_df=1, max_features=3000,
            norm='l2', encoding="shift_jis"
        )


        # ファイル名で渡すので、inputにfilename指定して初期化
        # max_dfは0.5（半分以上の文書に出現する言葉はいらん）を設定
        count_vectorizer = CountVectorizer(
            input='filename', max_df=0.5, min_df=1, max_features=3000,
            encoding="shift_jis"
        )

        # 全ファイルパスを入れた変数でfit_transform
        files = ['wakati/' + path for path in os.listdir('wakati')]
        tf = count_vectorizer.fit_transform(files)

        # shapeは8(doc count) * 3000(max_features)になっていた
        # tf.shape
        # => (8, 3000)

        # featue_name一覧を取得
        features = count_vectorizer.get_feature_names()
        # features[0:5]
        # => ['0213', '10月25日', '13', '1980', '1989']

        # index:100〜104までの5つの単語について、各ドキュメントの出現数を出す。
        # 8つの文書を読ませたので、8文書*5文字のmatrixになっている
        # tf.toarray()[:, 100:105]


        # 全ファイルパスを入れた変数でfit_transform
        files = ['wakati/' + path for path in os.listdir('wakati')]
        tfidf = tfidf_vectorizer.fit_transform(files)
        # feature_name一覧
        feature_names = tfidf_vectorizer.get_feature_names()

        if os.path.exists("CSV") == False:
            os.mkdir("CSV")
        # カムパネルラの値
        number = len(os.listdir(os.getcwd()+'/wakati/'))
        for file_number in range(number):
            all_list = []
            for j in feature_names:
                test = []
                word_result = tfidf.toarray()[:, features.index(j)]
                tf_value = word_result[file_number]
                test.append(j)
                test.append(tf_value)
                all_list.append(test)
            sort_list = sorted(all_list,key=lambda x:x[1],reverse=True)
            file_namesd = files[file_number].split("/")[1].split(".")[0]
            with open("CSV/"+file_namesd+".csv","a") as fd:
                for s in sort_list:
                    fd.write(str(s[0])+","+str(s[1])+"\n")
            


        # => array([ 0. ,  0. ,  0. ,  0. ,  0. , 0. ,  0.43341484,  0. ])

        # ジョバンニの値
        # tfidf.toarray()[:, features.index('ジョバンニ')]
        # => array([ 0. ,  0. ,  0. ,  0. ,  0. , 0. ,  0.81533485,,  0. ])
