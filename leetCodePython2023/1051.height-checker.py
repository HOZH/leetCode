#
# @lc app=leetcode id=1051 lang=python3
#
# [1051] Height Checker
#

# @lc code=start
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # expected = sorted(heights)
        # return len(list(filter(lambda x: heights[x] != expected[x], [i for i in range(len(heights))])))
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))
# @lc code=end
