#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
from heapq import heapify, heappop


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        num_count = len(unique_nums)
        if not num_count:
            return 0
        if num_count <= 2:
            return max(unique_nums)
        heap = list(map(lambda x: -x, unique_nums))
        heapify(heap)
        for _ in range(2):
            heappop(heap)

        return -heappop(heap)


# @lc code=end