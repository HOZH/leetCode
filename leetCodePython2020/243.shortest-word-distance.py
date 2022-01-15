#
# @lc app=leetcode id=243 lang=python3
#
# [243] Shortest Word Distance
#

# @lc code=start
from itertools import product


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        list_1, list_2 = [], []
        for i in range(len(wordsDict)):
            current = wordsDict[i]
            if current == word1:
                list_1.append(i)
            elif current == word2:
                list_2.append(i)
        temp = []
        for i in list_1:
            for j in list_2:
                temp.append((i, j))

        return min(list(map(lambda x: abs(x[0]-x[1]), temp)))

# printing unique_combination list
# @lc code=end
