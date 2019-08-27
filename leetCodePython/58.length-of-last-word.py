#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        temp = s.split()
        return 0 if len(temp)==0 else len(temp[-1])


