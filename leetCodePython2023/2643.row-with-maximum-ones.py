#
# @lc app=leetcode id=2643 lang=python3
#
# [2643] Row With Maximum Ones
#

# @lc code=start
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_count = 0
        row_index = 0
        for i, row in enumerate(mat):
            count = row.count(1)
            if max_count < count:
                max_count = count
                row_index = i

        return [row_index, max_count]


# @lc code=end
