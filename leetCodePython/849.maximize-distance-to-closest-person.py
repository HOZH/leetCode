#
# @lc app=leetcode id=849 lang=python3
#
# [849] Maximize Distance to Closest Person
#


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        count = 0
        current = 0

        leading_0 = True
        leading = 0
        for i in range(len(seats)):

            if seats[i] == 0:

                current += 1
                if leading_0:
                    leading += 1

            if seats[i] == 1:

                leading_0 = False

                count = current if current >= count else count

                current = 0

        return max(current, leading, math.ceil(count/2))
