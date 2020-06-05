#
# @lc app=leetcode id=1051 lang=python3
#
# [1051] Height Checker
#

# @lc code=start


class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        return sum(x != y for (x, y) in zip(sorted(heights), heights))


# @lc code=end
