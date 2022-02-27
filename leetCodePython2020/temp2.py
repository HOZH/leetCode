""""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.


Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
Output: [[1, 6], [8, 10], [15, 18]]
Explanation: Since intervals[1, 3] and [2, 6] overlaps, merge them into[1, 6].


Input: intervals = [[1, 4], [4, 5]]
Output: [[1, 5]]
Explanation: Intervals[1, 4] and [4, 5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""""


def solution(intervals):
    intervals.sort()
    """O(NlogN)"""
    ans = []
    """O(N)"""
    for interval in intervals:
        """check overlapping"""
        if ans and interval[0] <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1], interval[1])
        else:
            ans.append(interval)
    return ans


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
