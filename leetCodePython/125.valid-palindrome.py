#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#


class Solution:
    def isPalindrome(self, s: str) -> bool:

        a = s.lower()

        c = [chr(x)
             for x in range(97, 123)]

        d = [chr(x)
             for x in range(48, 58)]

        e = set(c+d)

        b = list(filter(lambda x: x in e, a))

        left, right = 0, len(b)-1

        while left <= right:

            if b[left] == b[right]:
                left += 1
                right -= 1

            else:
                return False

        return True
