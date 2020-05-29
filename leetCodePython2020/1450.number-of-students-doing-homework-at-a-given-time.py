#
# @lc app=leetcode id=1450 lang=python3
#
# [1450] Number of Students Doing Homework at a Given Time
#

# @lc code=start


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:

        result = 0
        for i in range(len(startTime)):

            if startTime[i] <= queryTime:

                if endTime[i] >= queryTime:
                    result += 1

            else:
                continue

        return result

# @lc code=end
