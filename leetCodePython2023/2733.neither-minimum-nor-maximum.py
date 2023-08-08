#
# @lc app=leetcode id=2733 lang=python3
#
# [2733] Neither Minimum nor Maximum
#

# @lc code=start
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        temp = set(nums)
        if len(temp)<3:
            return -1
        temp.remove(min(temp))
        temp.remove(max(temp))
        return temp.pop()
        
# @lc code=end

