#
# @lc app=leetcode id=3492 lang=python3
#
# [3492] Maximum Containers on a Ship
#

# @lc code=start
class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        count = min(maxWeight//w, n**2)
        return count

# @lc code=end
