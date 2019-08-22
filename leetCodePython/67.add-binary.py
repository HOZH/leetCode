#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#


class Solution:
    def addBinary(self, a: str, b: str) -> str:

        max_length = len(a) if len(a) > len(b) else len(b)
        a, b = int(a), int(b)
        c = 0
        digit = 0
        for i in range(max_length):

            current = a % (10)
            a = a//10

            c += current*(2**digit)

            current = b % (10)
            b = b//10

            c += current*(2**digit)

            digit += 1

        result = ''

        while c != 0:

            current = c % 2

            c = c//2

            result = str(current)+result

        return result if result != "" else "0"
