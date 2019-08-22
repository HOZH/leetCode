#
# @lc app=leetcode id=970 lang=python3
#
# [970] Powerful Integers
#


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:

        lis = set()
        
        a, b, c, d = 0, 0, 0, 0

        while a < bound:

            a = x**b

            b += 1

            while True:

                c = y**d

                d += 1
                temp = a+c
                if temp <= bound:
                    lis.add(temp)
                else:
                    d = 0
                    break

                if y == 1:
                    break
            if x == 1:
                break
        lis = list(lis)

        return lis
