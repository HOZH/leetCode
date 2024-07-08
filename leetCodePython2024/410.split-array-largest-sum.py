#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)

        def helper(threshold):
            count = 1
            total = 0
            for num in nums:
                total += num
                if total > threshold:
                    total = num
                    count += 1
                    if count > k:
                        return False
            return True

        while left < right:
            mid = left+(right-left)//2
            if helper(mid):
                right = mid
            else:
                left = mid+1

        return left
# @lc code=end
