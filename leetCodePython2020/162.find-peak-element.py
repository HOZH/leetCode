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
            m = l + (r-l)//2

            if nums[m] > nums[m+1]:
                r = m

            else:
                l = m+1
        return l

# @lc code=end
