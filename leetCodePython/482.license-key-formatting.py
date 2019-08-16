#
# @lc app=leetcode id=482 lang=python3
#
# [482] License Key Formatting
#


class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:

        s = S.replace('-', '', -1).upper()

        remainder = len(s) % K

        string = s[:remainder]
        if remainder != 0:
            string += '-'
        s = s[remainder:]

        for i in range(len(s)):

            string += s[i]
            if (i+1) % K == 0:
                string += '-'

        return string[:-1]
