#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#

# from collections import *


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        counter = collections.Counter(arr1)

        lis, lis1 = list(), list()
        length = len(arr1)

        for i in arr2:

            for j in range(counter[i]):
                lis.append(i)

        for i in arr1:

            if i not in arr2:
                lis1.append(i)

        lis1.sort()
        return lis+lis1
