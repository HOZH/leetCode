#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
from heapq import heappop, heapify


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negative_nums = [-i for i in nums]

        heapify(negative_nums)

        negative_ans = None
        for i in range(k):
            negative_ans = heappop(negative_nums)

        return -negative_ans


# @lc code=end
