#
# @lc app=leetcode id=1351 lang=python3
#
# [1351] Count Negative Numbers in a Sorted Matrix
#

# @lc code=start
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(list(map(lambda l: list(map(lambda x: True if x < 0 else False, l)).count(True), grid)))

# @lc code=end
