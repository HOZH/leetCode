#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        len1, len2 = len(word1), len(word2)
        if len(word1) == 0:
            return len2
        if len2 == 0:
            return len1

        # table = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        table = [[0] * (len(word2)+1) for j in range(len(word1)+1)]

        # initial values
        for i in range(len1+1):
            table[i][0] = i

        for i in range(len2+1):
            table[0][i] = i

        # opt = [0, 0, 0]  # match, ?sub, insert, delete

        for i in range(1, len(table)):
            for j in range(1, len(table[0])):
                table[i][j] = min(table[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1),
                                  table[i][j-1]+1, table[i-1][j]+1)
                # matched = 0 if word1[i-1] == word2[j-1] else 1
                # opt[0] = table[i-1][j-1] + matched
                # opt[1] = table[i][j-1]+1
                # opt[2] = table[i-1][j]+1

                # table[i][j] = opt[0]

                # for k in range(3):
                #     if opt[k] < table[i][j]:
                #         table[i][j] = opt[k]

        return table[-1][-1]

# @lc code=end
