#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        length = len(flowerbed)
        for i in range(length):

            if n == 0:
                return True

            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i-1] == 0) and (i == (length-1) or flowerbed[i+1] == 0):

                    flowerbed[i] = 1

                    n -= 1

        return True if n <= 0 else False
