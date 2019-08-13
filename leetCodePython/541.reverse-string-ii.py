#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        length = len(s)
        if length == 0:
            return 0

        s = [i for i in s]

        for i in range(0, length, 2*k):

            key = i+k

            s[i:key] = s[i:key][::-1]

        return "".join(s)
