#
# @lc app=leetcode id=2656 lang=python3
#
# [2656] Maximum Sum With Exactly K Elements 
#

# @lc code=start
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        local_max = max(nums)
        result = 0
        for i in range(k):
            result+=i
        result+=(local_max*k)
        return result

        
# @lc code=end

