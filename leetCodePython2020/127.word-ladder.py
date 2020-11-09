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

        if endWord not in wordList:
            return 0

        queue = deque([beginWord])

        step = 0
        local_set = set()

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

                                if temp not in local_set:
                                    if temp == endWord:
                                        return step + 1
                                    else:
                                        queue.append(temp)
                                        local_set.add(temp)
        return 0


# @lc code=end
