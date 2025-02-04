#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
from collections import deque


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        depthMap = {}
        ans = []

        def dfs(word, seq):
            if word == beginWord:
                ans.append(seq[::-1])
                return

            steps = depthMap[word]
            for i in range(len(word)):
                original = word[i]
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    word = word[:i] + ch + word[i+1:]
                    if word in depthMap and depthMap[word] + 1 == steps:
                        seq.append(word)
                        dfs(word, seq)
                        seq.pop()
                word = word[:i] + original + word[i+1:]

        wordSet = set(wordList)
        q = deque([beginWord])
        depthMap[beginWord] = 1
        wordSet.discard(beginWord)

        while q:
            word = q.popleft()
            steps = depthMap[word]
            if word == endWord:
                break
            for i in range(len(word)):
                original = word[i]
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    word = word[:i] + ch + word[i+1:]
                    if word in wordSet:
                        q.append(word)
                        wordSet.discard(word)
                        depthMap[word] = steps + 1
                word = word[:i] + original + word[i+1:]

        if endWord in depthMap:
            seq = [endWord]
            dfs(endWord, seq)

        return ans
# @lc code=end

