#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 0:
            return []
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        for i in intervals[1:]:
            start, end = i
            if ans[-1][1] >= start:
                ans[-1][0] = min(ans[-1][0], start)
                ans[-1][1] = max(ans[-1][1], end)
            else:
                ans.append([start, end])

        return ans


# @lc code=end
