#
# @lc app=leetcode id=1266 lang=python3
#
# [1266] Minimum Time Visiting All Points
#

# @lc code=start


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        steps = 0

        for i in range(len(points) - 1):
            current = points[i]
            approaching = points[i + 1]

            h_diff = abs(current[0] - approaching[0])
            v_diff = abs(current[1] - approaching[1])

            steps += min(h_diff, v_diff) + abs(h_diff - v_diff)

        return steps
# @lc code=end
