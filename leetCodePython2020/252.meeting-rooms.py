#
# @lc app=leetcode id=252 lang=python3
#
# [252] Meeting Rooms
#

# @lc code=start
class Solution:
    # def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    #     array = [0]*(10**6+1)
    #     for start, end in intervals:   O(n)
    #         for i in range(start, end):    O (len of interval)
    #             if array[i] == 1:
    #                 return False
    #             array[i] = 1
    #     return True
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort() 
        """O(num of intervals * log (numof intervals))"""
        for i in range(1, len(intervals)):
            last, current = intervals[i-1], intervals[i]
            if current[0] < last[1]:
                return False
        return True

# @lc code=end
