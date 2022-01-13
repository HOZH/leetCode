#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:

        consecutive_lates, absents = 0, 0
        for i in s:
            if i == 'L':
                consecutive_lates += 1
                if consecutive_lates > 2:
                    return False
            else:
                consecutive_lates = 0
                if i == 'A':
                    absents += 1
                if absents > 1:
                    return False
        return True

# @lc code=end
