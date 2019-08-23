#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        next_location = 0

        temp_list = list()

        for i in nums2:

            for j in range(next_location, m):

                if i > nums1[j]:
                    temp_list.append(nums1[j])
                    next_location += 1

                else:

                    break
            temp_list.append(i)

        for i in range(next_location, m):

            temp_list.append(nums1[i])

        if len(temp_list) == 0:
            return
        for i in range(len(nums1)):

            nums1[i] = temp_list[i]
