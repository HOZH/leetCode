#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def possible(K):
            return sum((p-1)//K + 1 for p in piles) <= H

        l, r = 1, max(piles)
        if H == len(piles):
            return r

        result = -1
        while l <= r:

            pivot = l + (r - l) // 2

            # temp = sum(
            #     list(map(lambda x: 1 if x <= pivot else (math.ceil(x / pivot)), piles)))

            # if temp <= H:
            if possible(pivot):
                r = pivot - 1
                result = pivot

            else:
                # 2 slow, increasing lower bound
                l = pivot + 1
        return result


# @lc code=end
