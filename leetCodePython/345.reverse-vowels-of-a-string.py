#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#


class Solution:
    def reverseVowels(self, s: str) -> str:

        rev = list()
        b = set(('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'))
        temp = ""
        for i in s:

            if i in b:
                temp += "{}"
                rev.append(i)

            else:
                temp += i

        rev = rev[::-1]

        return temp.format(*rev)
