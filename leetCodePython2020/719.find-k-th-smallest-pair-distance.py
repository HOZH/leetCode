#
# @lc app=leetcode id=719 lang=python3
#
# [719] Find K-th Smallest Pair Distance
#

# @lc code=start
from collections import defaultdict, Counter
import math


class Solution:

    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        # nums.sort()
        # N = nums[-1]
        # # buckets
        # count = [0 for _ in range(N + 1)]
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         count[nums[j] - nums[i]] += 1

        # for i in range(N):
        #     k -= count[i]
        #     if k <= 0:
        #         return i

        # return 0

        nums.sort()
        n = len(nums)

        l, r = 0, nums[-1]-nums[0]

        while l <= r:
            count = 0

            j = 0

            m = l + (r-l)//2

            for i in range(n):
                while (j < n and nums[j]-nums[i] <= m):
                    # increase j until nums[j] - nums[i] >m
                    j += 1
                # not zeroed out => count = previous count+ j-i-1
                count += j - i - 1

            if count >= k:
                r = m-1
            else:
                l = m+1
        return l

# @lc code=end
