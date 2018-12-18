# p-*- coding: utf-8 -*-

import os
import MeCab

class Wakatis():
    def __init__(self):
        # 分かち書きしたファイル格納用のディレクトリ
        if not os.path.exists('wakati'):
            os.mkdir('wakati')

        self.tagger = MeCab.Tagger()
        self.tagger.parseToNode('')


    def lineWakatiWriter(self, line, writer):
        node = self.tagger.parseToNode(line)
        while node:
            if node.feature.startswith('名詞'):
                writer.write(node.surface + '\n')
            node = node.next

    def main(self):
        for file in os.listdir('data'):
            with open('data/' + file, 'r', encoding='shift_jis') as reader, open('wakati/' + file, 'w', encoding='shift_jis') as writer:
                # with open('aozora/' + file, 'r') as reader:
                for line in reader:
                    self.lineWakatiWriter(line, writer)


