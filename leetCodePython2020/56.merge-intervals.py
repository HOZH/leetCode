#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start

# Hong
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not len(intervals):
            return []
        intervals.sort()

        result = [intervals[0]]
        for current in intervals[1:]:
            current_head, current_tail = current[0], current[1]
            prev_head, prev_tail = result[-1][0], result[-1][1]

            if current_head <= prev_tail:
                # remove last interval and append the new combined one into result list
                result = result[:-1]
                result.append([prev_head, max(prev_tail, current_tail)])
            else:
                # append the original interval if not overlapping
                result.append(current)

        return result

# @lc code=end
