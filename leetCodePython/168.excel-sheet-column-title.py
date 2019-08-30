#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title

#


class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = ""
        while n > 0:
            ans = chr(65 + ((n-1) % 26))+ans
            n = (n-1) // 26

        return ans
