#
# @lc app=leetcode id=2391 lang=python3
#
# [2391] Minimum Amount of Time to Collect Garbage
#

# @lc code=start
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        if len(garbage) == 0:
            return 0
        prev_g, prev_p, prev_m = 0, 0, 0
        total_time = len(garbage[0])
        for i in range(1, len(garbage)):
            travel_time = travel[i-1]
            current = garbage[i]
            g_count = current.count('G')
            p_count = current.count('P')
            m_count = current.count('M')
            total_time += g_count+p_count+m_count+travel_time*3
            if g_count:
                prev_g = i
            if p_count:
                prev_p = i
            if m_count:
                prev_m = i
        for i in range(len(garbage)-1, -1, -1):
            travel_time = travel[i-1]
            if prev_g < i:
                total_time -= travel_time
            if prev_p < i:
                total_time -= travel_time
            if prev_m < i:
                total_time -= travel_time
        return total_time


# @lc code=end
