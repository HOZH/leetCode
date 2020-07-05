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
        while len(queue) > 0:
            local_set = set()
            # print(queue)
            step += 1
            # if step > self.default_len+1:
            #     break

            for k in range(len(queue)):
                    current = queue.popleft()
                # print(current)
                    if current == endWord:
                        return step + 1

                # if 1 == 1:

                    # if current not in self.pos_cache:
                    #     self.pos_cache[current] = []

                    for i in range(len(current)):
                        for j in range(97, 123):
                            ch = chr(j)
                            if ch != current[i]:
                                temp = current[:i] + ch + current[i + 1:]
                                # temp = [*current]
                                # temp[i]=ch
                                # temp = ''.join(temp)
                                if temp in wordList:
                                    wordList.remove(temp)

                                    if temp not in local_set:
                                        # if temp in wordList:
                                        if temp == endWord:
                                            return step + 1
                                        else:
                                            # if temp not in local_set:
                                            # self.pos_cache[current].append(temp)
                                            queue.append(temp)
                                            local_set.add(temp)

                # else:
                    # print('used')

                    # queue.extend(self.pos_cache[current])

        return 0
# @lc code=end
