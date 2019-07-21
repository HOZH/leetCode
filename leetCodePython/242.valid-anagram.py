#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_len = len(s)
        if s_len != len(t):
            return False

        else:

            dic1 = dict()
            dic2 = dict()

            for i in range(s_len):

                if s[i] in dic1:

                    dic1[s[i]] += 1

                else:

                    dic1[s[i]] = 1

                if t[i] in dic2:

                    dic2[t[i]] += 1

                else:

                    dic2[t[i]] = 1

            return dic1 == dic2
