#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
from heapq import heapify, heappop, heappush


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if len(stones) == 1:
            return stones[0]

        stones = list(map(lambda x: 0-x, stones))

        heapify(stones)

        while len(stones) > 1:

            x = heappop(stones)
            y = heappop(stones)

            z = -abs(x-y)

            heappush(stones, z)

        return -stones[0]


# @lc code=end
