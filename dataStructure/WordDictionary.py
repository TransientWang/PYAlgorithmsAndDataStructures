# -*- coding: UTF-8 -*-
class WordDictionary(object):

    def __init__(self):
        """
        211. 添加与搜索单词 - 数据结构设计
        前缀树+回溯
        Initialize your data structure here.
        """
        self.root = dict()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        t = self.root
        for i in word:
            if i not in t:
                t[i] = {}
            t = t[i]
        t["#"] = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """

        def find(word=word, t=self.root):
            if word == "":
                if "#" in t:
                    return True
                return False
            if len(t) == 1 and "#" in t and len(word) > 0:
                return False
            if word[0] in t and word[0] != "." and find(word[1:], t[word[0]]):
                return True
            if word[0] == ".":
                for i in t.keys():
                    if i != "#" and find(word[1:], t[i]):
                        return True
            return False

        return find()


if __name__ == '__main__':
    o = WordDictionary()
    o.addWord("a")
    o.addWord("ab")

    print(o.search("a"))
    print(o.search("a."))
    # print(o.search("ab"))
    # print(o.search(".a"))
    # print(o.search(".b"))
    # print(o.search("ab."))
    # print(o.search("."))
    # print(o.search(".."))
