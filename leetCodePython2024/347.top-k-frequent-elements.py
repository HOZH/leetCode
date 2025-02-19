#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import Counter
from heapq import heappop, heappush


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for key, count in counter.items():
            heappush(heap, (-count, key))

        ans_count = 0
        ans = []
        while ans_count < k:
            ans.append(heappop(heap)[1])
            ans_count += 1
        return ans

# @lc code=end
