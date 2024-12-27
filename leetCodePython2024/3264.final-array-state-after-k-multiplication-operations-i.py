#
# @lc app=leetcode id=3264 lang=python3
#
# [3264] Final Array State After K Multiplication Operations I
#

# @lc code=start
from heapq import heapify, heappop, heappush


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = [(val, i) for i, val in enumerate(nums)]
        heapify(pq)

        for _ in range(k):
            _, i = heappop(pq)
            nums[i] *= multiplier
            heappush(pq, (nums[i], i))

        return nums

        # len_nums = len(nums)
        # for _ in range(k):
        #     min_index = 0
        #     for j in range(1, len_nums):
        #         if nums[j] < nums[min_index]:
        #             min_index = j
        #     nums[min_index] *= multiplier

        # return nums


# @lc code=end
