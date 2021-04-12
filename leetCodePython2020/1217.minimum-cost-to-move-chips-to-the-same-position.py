#
# @lc app=leetcode id=1217 lang=python3
#
# [1217] Minimum Cost to Move Chips to The Same Position
#

# @lc code=start
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = 0
        for i in position:
            if(i % 2 == 0):
                even += 1
        return min(even, len(position)-even)

# @lc code=end
