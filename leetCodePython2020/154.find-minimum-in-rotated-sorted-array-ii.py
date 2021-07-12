#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:

        def helper(arr, l, r):
            if l+1 >= r:
                return min(arr[l], arr[r])

            if arr[l] < arr[r]:
                return arr[l]

            m = l + (r-l)//2

            return min(helper(arr, l, m-1), helper(arr, m, r))

        return helper(nums, 0, len(nums)-1)

# @lc code=end
