#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start

from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums):

        dp = [0]*len(nums)
        for i in range(len(nums)):
            
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i],dp[j])
            dp[i]+=1
        return max(dp)

    def lengthOfLI1S(self, nums):

        if len(nums) == 0:
            return 0

        tails = [float('inf')]*len(nums)

        for i in nums:

            current_index = bisect_left(tails, i)

            tails[current_index] = i

        return len(list(filter(lambda x: x != float('inf'), tails)))

    # (1) if x is larger than all tails, append it, increase the size by 1
    # (2) if tails[i-1] < x <= tails[i], update tails[i]

    def lengthOfLIS_bs(self, nums):
        if len(nums) == 0:
            return 0
        tails = [0]*len(nums)
        # [4, 5, 6, 3],
        # tails[i] -> min ending number with i+1 length of IS
        # len = 1   :      [4], [5], [6], [3]   => tails[0] = 3
        # len = 2:      [4, 5], [5, 6] = > tails[1] = 5
        # len = 3:      [4, 5, 6] = > tails[2] = 6

        # [4]
        # [4][5]
        # [4][5][6]
        # [3][5][6]
        # return 3
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = i+(j-i)//2
                if tails[m] < x:
                    i = m+1
                elif tails[m] >= x:

                    j = m
            tails[i] = x
            size = max(i+1, size)
        return size

    def lengthOfLIS_dp(self, nums):
        if len(nums) == 0:
            return 0
        dp = [1]*len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


# @lc code=end
