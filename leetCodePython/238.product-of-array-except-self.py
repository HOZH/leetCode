#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = [1]

        right = [1]

        length = len(nums)

        temp = length-1

        for i in range(temp):

            left.append(left[-1]*nums[i])
            right.append(right[-1]*nums[temp-i])

        ans = list()
        for i in range(length):

            ans.append(left[i]*right[temp-i])

        return ans
