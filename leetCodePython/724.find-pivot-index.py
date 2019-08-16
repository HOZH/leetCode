#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        # length = len(nums)
        # dic = dict()
        # right_dic = dict()

        # right_total = 0
        # total = 0
        # max_indice = length-1
        # for i in range(length):
        #     dic[i] = total
        #     right_dic[max_indice-i] = right_total
        #     total += nums[i]
        #     right_total += nums[max_indice-i]

        # for i in range(length):

        #     if dic[i] == right_dic[i]:
        #         return i

        s = sum(nums)

        left_sum = 0

        for i, x in enumerate(nums):

            if left_sum == s-left_sum-x:

                return i

            left_sum += x

        return -1
