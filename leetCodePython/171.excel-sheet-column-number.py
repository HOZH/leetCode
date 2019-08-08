#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#
class Solution:
    def titleToNumber(self, s: str) -> int:

        answer=0


        for i in s:

            answer*=26
            answer+=ord(i)-64

        return answer


        

