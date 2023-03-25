#
# @lc app=leetcode id=1550 lang=python3
#
# [1550] Three Consecutive Odds
#

# @lc code=start
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        count = 0
        for i in arr:
            if i % 2 == 0:
                count = 0
            else:
                count += 1

            if count == 3:
                return True

        return False

# @lc code=end
