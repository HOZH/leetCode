#
# @lc app=leetcode id=487 lang=python3
#
# [487] Max Consecutive Ones II
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        first_zero = -1

        count, max_count = 0, 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            elif nums[i] == 0 and first_zero == -1:
                count += 1
                first_zero = i
            else:
                max_count = max(max_count, count)
                count = i-first_zero
                first_zero = i
        max_count = max(max_count, count)
        return max_count
# @lc code=end
