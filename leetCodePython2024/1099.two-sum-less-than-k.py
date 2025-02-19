#
# @lc app=leetcode id=1099 lang=python3
#
# [1099] Two Sum Less Than K
#

# @lc code=start
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = -1
        left = 0
        right = len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if (sum < k):
                answer = max(answer, sum)
                left += 1
            else:
                right -= 1
        return answer
        
# @lc code=end

