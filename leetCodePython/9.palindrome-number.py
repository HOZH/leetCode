#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#


class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        s = str(x)

        while len(s) > 1:

            if s[0] == s[-1]:

                s = s[1:-1]

            else:
                return False

        return True
