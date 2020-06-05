#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        temp = list()
        for i in range(len(mat)):
            count = 0
            for j in mat[i]:
                if j == 1:
                    count += 1
                else:
                    break
            temp.append((count, i))

        return list(map(lambda x: x[1], sorted(temp)[:k]))


# @lc code=end
