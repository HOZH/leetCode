#
# @lc app=leetcode id=832 lang=python3
#
# [832] Flipping an Image
#

# @lc code=start


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        x, y = len(A[0]), len(A)

        result = []
        for i in range(y):

            current = []

            for j in range(x):
                current.append(0 if A[i][x-j-1] else 1)
            result.append(current)

        return result

# @lc code=end
