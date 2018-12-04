import os
import MeCab

class Load():
    def __init__(self):
        """
        mecabのsetting
        """
        self.tagger = MeCab.Tagger()
        self.tagger.parseToNode('')

    def analysis(self,node):
        """
        一つのファイルデータからの解析を行う
        Args: node

        Return: word
        """
        worde_list = []
        while node:
            if node.feature.startswith('名詞'):
                worde_list.append(node.surface)
            node = node.next
        return "\n".join(worde_list)

    def load_data(self):
        """
        ファイルから解析した値をリスト構造で返す.
        [one file data] <- [file list]
        ファイルごとをリストとして持っており，その中に一つのファイルデータがある．
        """
        one_file_data = []
        file_data = []
        for file_name in os.listdir('data'):
            with open('data/' + file_name, 'r', encoding='shift_jis') as reader:
                for data in reader:
                    node = self.tagger.parseToNode(data)
                    word = self.analysis(node)
                    one_file_data.append(word)
        file_data.append(one_file_data)
        return file_data

if __name__ == "__main__":
    loading = Load()
    test = loading.load_data()
    print(test)
