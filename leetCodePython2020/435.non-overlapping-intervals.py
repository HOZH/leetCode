#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
from heapq import heapify, heappop, heappush


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        sort_by_end = list(map(lambda x: [x[1], x[0]], intervals))
        sort_by_start = intervals[:]
        heapify(sort_by_start)
        heapify(sort_by_end)

        count = 0

        while sort_by_start:

            current = heappop(sort_by_end)
            count += 1

            while sort_by_start:

                temp = heappop(sort_by_start)
                if temp[0] >= current[0]:
                    heappush(sort_by_start, temp)
                    break

            while sort_by_end:
                temp = heappop(sort_by_end)
                if temp[1] >= current[0]:
                    heappush(sort_by_end, temp)
                    break
        return len(intervals)-count

    def eraseOverlapIntervals_temp(self, intervals: List[List[int]]) -> int:

        availables = [i for i in range(len(intervals))]

        count = 0
        while availables:
            current_index = min(availables, key=lambda x: intervals[x][1])
            count += 1
            availables = list(
                filter(lambda x: intervals[x][0] >= intervals[current_index][1], availables))

        return len(intervals)-count


# @lc code=end
