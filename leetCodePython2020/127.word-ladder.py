#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start

from collections import deque


class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:

        s1 = set([beginWord])
        s2 = set([endWord])

        wordList = set(wordList)

        if endWord not in wordList:
            return 0

        step = 0

        while s1 and s2:

            step += 1
            if len(s1) > len(s2):
                temp = s1
                s1 = s2
                s2 = temp

            s = set()

            for current in s1:
                for i in range(len(current)):
                    for j in range(97, 123):
                        # find next potential word in wordlist
                        ch = chr(j)
                        if ch != current[i]:
                            temp = current[:i] + ch + current[i + 1:]

                            if temp in s2:
                                return step+1

                            if temp in wordList:
                                s.add(temp)
                                wordList.remove(temp)

            s1 = s

        return 0

    def ladderLength_temp(self, beginWord: str, endWord: str, wordList) -> int:
        self.default_len = len(wordList)
        wordList = set(wordList)
        self.pos_cache = dict()

        if endWord not in wordList:
            return 0

        queue = deque([beginWord])

        step = 0

        # bfs
        while len(queue) > 0:
            step += 1

            current_layer_len = len(queue)

            for _ in range(current_layer_len):
                current = queue.popleft()
                if current == endWord:
                    return step + 1

                for i in range(len(current)):
                    for j in range(97, 123):
                        # find next potential word in wordlist
                        ch = chr(j)
                        if ch != current[i]:
                            temp = current[:i] + ch + current[i + 1:]

                            if temp in wordList:
                                wordList.remove(temp)

                                if temp == endWord:
                                    return step + 1
                                else:
                                    queue.append(temp)
        return 0


# @lc code=end
