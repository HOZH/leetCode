#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#


class Solution:
    def convertToBase7(self, num: int) -> str:

        if num == 0:

            return '0'

        if num < 0:
            result = '-'

            num = abs(num)

        else:

            result = ''

        lim = int(math.log(num, 7))

        for i in range(lim, -1, -1):

            temp = 7**i
            dumped = num//temp
            result += str(dumped)
            num -= dumped*temp

        return result
