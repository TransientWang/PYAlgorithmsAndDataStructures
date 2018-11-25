# -*- coding: UTF-8 -*-
class Trie(object):

    def __init__(self):
        self.__root__ = {}


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curNode = self.__root__
        for i in word:
            if i not in curNode:
                curNode[i] = {}
            curNode = curNode[i]
        curNode["#"] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curNode = self.__root__
        for i in word:
            if i not in curNode:
                return False
            curNode = curNode[i]
        if "#" not in curNode:
            return False
        return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curNode = self.__root__
        for i in prefix:
            if i not in curNode:
                return False
            curNode = curNode[i]
        return True
