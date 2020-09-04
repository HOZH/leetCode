#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start

from collections import deque


class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        self.default_len = len(wordList)
        wordList = set(wordList)
        self.pos_cache = dict()

        def matched(a, b):
            count = 0
            for i in range(len(a)):
                if a[i] == b[i]:
                    continue
                else:
                    count += 1

        if endWord not in wordList:
            return 0

        queue = deque([beginWord])

        step = 0
        while len(queue) > 0:
            local_set = set()
            step += 1

            for _ in range(len(queue)):
                current = queue.popleft()
                if current == endWord:
                    return step + 1

                for i in range(len(current)):
                    for j in range(97, 123):
                        ch = chr(j)
                        if ch != current[i]:
                            temp = current[:i] + ch + current[i + 1:]

                            if temp in wordList:
                                wordList.remove(temp)

                                if temp not in local_set:
                                    if temp == endWord:
                                        return step + 1
                                    else:
                                        queue.append(temp)
                                        local_set.add(temp)
        return 0


# @lc code=end
