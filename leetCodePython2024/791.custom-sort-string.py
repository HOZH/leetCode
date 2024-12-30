#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#

# @lc code=start
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        return ''.join(sorted([*s], key=lambda x: order.index(x) if x in order else 26))

# @lc code=end
