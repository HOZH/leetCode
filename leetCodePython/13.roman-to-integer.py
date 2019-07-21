#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#


class Solution:
    def romanToInt(self, s: str) -> int:

        num = 0

        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        n = len(s)

        skip = False

        if n % 2 != 0:
            s += 'I'

        for i in range(n):

            if skip:
                skip = False
                continue

            if i == (n - 1):

                num += dic[s[n-1]]
                break

            if dic[s[i]] >= dic[s[i + 1]]:

                num += dic[s[i]]

            else:

                num += dic[s[i + 1]] - dic[s[i]]

                skip = True

        return num
