#
# @lc app=leetcode id=1991 lang=python3
#
# [1991] Find the Middle Index in Array
#

# @lc code=start
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        current_sum = 0

        for i in range(len(nums)):
            if (total-nums[i]) / 2 == current_sum:
                return i
            current_sum += nums[i]

        return -1

# @lc code=end
