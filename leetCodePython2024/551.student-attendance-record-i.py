#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        absent_count = 0
        late_count = 0
        for i in s:
            if i == 'L':
                late_count += 1
                if late_count > 2:
                    return False
            else:
                if i == 'A':
                    absent_count += 1
                late_count = 0

            if absent_count > 1:
                return False

        return True


# @lc code=end
