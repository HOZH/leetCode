#
# @lc app=leetcode id=826 lang=python3
#
# [826] Most Profit Assigning Work
#

# @lc code=start
from functools import lru_cache


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker = sorted(worker, reverse=True)
        difficulty_profit_pair = []
        for i in range(len(difficulty)):
            difficulty_profit_pair.append((difficulty[i], profit[i]))
        difficulty_profit_pair.sort()
        difficulty, profit = [], []
        for i in range(len(difficulty_profit_pair)):
            difficulty.append(difficulty_profit_pair[i][0])
            profit.append(difficulty_profit_pair[i][1])

        @lru_cache(maxsize=None)
        def binary_search(capability, l, r):
            while l < r:
                mid = l+(r-l)//2
                if difficulty[mid] > capability:
                    r = mid
                else:
                    l = mid+1
            return l
        ans = 0
        left, right = 0, len(difficulty)-1
        for i in worker:
            boundary = binary_search(i, left, right)
            right_end = boundary if (
                difficulty[boundary] > i) else (boundary+1)
            local_max = max([0]+profit[:right_end])
            ans += local_max
            left = 0
            right = boundary

        return ans


# @lc code=end
