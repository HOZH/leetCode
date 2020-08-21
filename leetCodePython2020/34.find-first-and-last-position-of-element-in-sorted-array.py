#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        length = len(nums)
        if length < 1:
            return [-1, -1]

        l, r = 0, length - 1
        l_result, r_result, index = 0, length - 1, -1
        while l <= r:
            m = l + (r - l) // 2
            current = nums[m]
            if current < target:
                l = m + 1
            else:
                r = m - 1
            if current == target:
                index = m

        l_result = index

        l, r = 0, length - 1
        index = -1
        while l <= r:
            m = l + (r - l) // 2
            current = nums[m]
            if current > target:
                r = m - 1
            else:
                l = m + 1
            if current == target:
                index = m

        r_result = index
        return [l_result, r_result]


# @lc code=end
