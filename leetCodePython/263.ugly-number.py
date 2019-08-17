#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#


class Solution:
    def isUgly(self, num: int) -> bool:

        if num < 1:
            return False
        if num == 1:
            return True

        def helper(n):

            divided_2 = n % 2 == 0
            divided_3 = n % 3 == 0
            divided_5 = n % 5 == 0

            lis = set()

            if divided_2:

                if n // 2 == 1:
                    return True

                lis.add(helper(n // 2))

                if True in lis:
                    return True

            if divided_3:

                if n // 3 == 1:
                    return True

                lis.add(helper(n // 3))
                if True in lis:
                    return True

            if divided_5:

                if n // 5 == 1:
                    return True

                lis.add(helper(n // 5))

            return True in lis

        return helper(num)
