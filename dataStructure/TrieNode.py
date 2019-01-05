# -*- coding: UTF-8 -*-
class Trie(object):

    def __init__(self):
        '''
        208.Trie树（前缀树、字典树）的基本性质可以归纳为：

        （1）根节点不包含字符，除根节点外每个节点只包含一个字符。

        （2）从根节点到某一个节点，路径上经过的字符连接起来，为该节点对应的字符串。

        （3）每个节点的所有子节点包含的字符串不相同。
        '''
        self.root = {}


def insert(self, word):
    """
    Inserts a word into the trie.
    :type word: str
    :rtype: void
    """
    curNode = self.root
    for i in word:
        if curNode.get(i, -1) == -1:
            curNode[i] = {}
        curNode = curNode[i]
    curNode["#"] = True


def search(self, word):
    """
    Returns if the word is in the trie.
    :type word: str
    :rtype: bool
    """
    curNode = self.root
    for i in word:
        if i not in curNode:
            return False
        curNode = curNode[i]
    if curNode.get("#", -1) != -1:
        return True
    return False


def startsWith(self, prefix):
    """
    Returns if there is any word in the trie that starts with the given prefix.
    :type prefix: str
    :rtype: bool
    """
    curNode = self.root
    for i in prefix:
        if i not in curNode:
            return False
        curNode = curNode[i]
    return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert("wong")
    print()
