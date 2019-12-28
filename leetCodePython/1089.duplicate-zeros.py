#
# @lc app=leetcode id=1089 lang=python3
#
# [1089] Duplicate Zeros
#


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        length = len(arr)

        zero_lis = list()

        for i in range(length):

            if arr[i] == 0:

                zero_lis.append(0)
                zero_lis.append(0)

            else:

                zero_lis.append(arr[i])

        for i in range(length):

            arr[i] = zero_lis[i]

        # a = arr[:]
        # index = 0
        # old_index = 0
        # while True:

        #     if old_index in zero_lis:

        #         for _ in range(2):

        #             arr[index] = 0
        #             index += 1

        #             if index == length:
        #                 return

        #     else:

        #         arr[index] = a[old_index]
        #         index += 1
        #         if index == length:
        #             return

        #     old_index += 1
