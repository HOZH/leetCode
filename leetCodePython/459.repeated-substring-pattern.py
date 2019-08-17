#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        length = len(s)

        if length != 1:

            for i in range(1, length):

                if length % i == 0:

                    if s[:i]*(length//i) == s:
                        # if s.count(s[:i]) == length//i:

                        return True

        return False
