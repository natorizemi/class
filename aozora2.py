from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import os

# 引数として、CountVectorizerとTfidfTransformerで使った双方の引数が指定できるようになっている
tfidf_vectorizer = TfidfVectorizer(
    input='filename', max_df=0.5, min_df=1, max_features=3000, norm='l2', encoding="shift_jis")


# ファイル名で渡すので、inputにfilename指定して初期化
# max_dfは0.5（半分以上の文書に出現する言葉はいらん）を設定
count_vectorizer = CountVectorizer(
    input='filename', max_df=0.5, min_df=1, max_features=3000, encoding="shift_jis")

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
#tf.toarray()[:, 100:105]


# 全ファイルパスを入れた変数でfit_transform
files = ['wakati/' + path for path in os.listdir('wakati')]
tfidf = tfidf_vectorizer.fit_transform(files)

# feature_name一覧
feature_names = tfidf_vectorizer.get_feature_names()

# カムパネルラの値
print("--")
print(tfidf.toarray()[:, features.index('老人')])
print("--")
print(tfidf.toarray()[:])
# => array([ 0. ,  0. ,  0. ,  0. ,  0. , 0. ,  0.43341484,  0. ])

# ジョバンニの値
#tfidf.toarray()[:, features.index('ジョバンニ')]
# => array([ 0. ,  0. ,  0. ,  0. ,  0. , 0. ,  0.81533485,,  0. ])
