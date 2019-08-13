#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#


class Solution:
    def checkRecord(self, s: str) -> bool:

        return s.count('A') < 2 and s.find('LLL') == -1
