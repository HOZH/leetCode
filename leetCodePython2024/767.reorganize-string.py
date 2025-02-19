#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
import heapq
from collections import defaultdict
class Solution:
    def reorganizeString(self, s: str) -> str:
        char_freq = defaultdict(int)
        for c in s:
            char_freq[c] += 1

        max_heap = [(-freq, char) for char, freq in char_freq.items()]
        heapq.heapify(max_heap)

        res = []
        prev_freq, prev_char = 0, ""

        while max_heap:
            freq, char = heapq.heappop(max_heap)
            res.append(char)

            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))

            freq += 1
            prev_freq, prev_char = freq, char
        
        # a -3, b -3
        # a,
        # a,b
        # a,b,a
        # a,b,a,b
        

        if len(res) != len(s):
            return ""

        return "".join(res)
# @lc code=end

