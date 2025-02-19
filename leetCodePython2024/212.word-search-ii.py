#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
import collections


class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.isWord = True

    def search(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
            if not node:
                return False
        return node.isWord


class Solution(object):
    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res

    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if 0 <= i < len(board) and 0 <= j < len(board[0]):
            tmp = board[i][j]
            node = node.children.get(tmp)
            if not node:
                return
            board[i][j] = "#"
            self.dfs(board, node, i+1, j, path+tmp, res)
            self.dfs(board, node, i-1, j, path+tmp, res)
            self.dfs(board, node, i, j-1, path+tmp, res)
            self.dfs(board, node, i, j+1, path+tmp, res)
            board[i][j] = tmp

# @lc code=end
