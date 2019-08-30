#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#


class Solution:
    def reverse(self, x: int) -> int:

        if x == 0:
            return 0
        is_negative = x < 0

        if is_negative:

            temp = str(x)[1:]

        else:

            temp = str(x)

        temp = temp[::-1]

        while True:

            if temp[0] == "0":

                temp = temp[1:]

            else:
                break
        if is_negative:

            temp = "-"+temp

        ans = int(temp)

        return ans if ans < 2**31-1 and ans > -(2**31) else 0
