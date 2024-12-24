#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] < nums[mid+1]:
                l = mid+1
            else:
                r = mid

        return l


# @lc code=end
