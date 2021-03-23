#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#

# @lc code=start

from collections import defaultdict


class Solution:

    def findNumberOfLIS(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        dp = [1]*len(nums)
        end_by_count = [1]*len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j]+1 > dp[i]:
                        # dp[i] = max(dp[i], dp[j]+1)
                        dp[i]=dp[j]+1
                        end_by_count[i] = end_by_count[j]

                    elif dp[j]+1 == dp[i]:
                        end_by_count[i] += end_by_count[j]

        max_seq_len = max(dp)

        result = 0
        for i in range(len(dp)):
            if dp[i] == max_seq_len:
                result += end_by_count[i]

        return result

    def findNumberOfLIS_temp(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        dp = [1] * len(nums)

        for i in range(1, len(nums)):

            for j in range(i):

                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        max_seq_len = max(dp)

        if max_seq_len == 1:
            return len(dp)

        tails = []

        for i in range(len(dp)):
            if dp[i] == max_seq_len:
                tails.append(i)

        d = defaultdict(list)

        for i in range(len(dp)):
            d[dp[i]].append(i)

        for i in d.keys():
            d[i].sort()

        @lru_cache(None)
        def helper(layer, index):

            if layer == 0:
                return 1

            temp = 0

            prev_value = nums[index]

            for i in d[layer]:
                if i < index:
                    if nums[i] < prev_value:
                        # if layer == 1:
                        #     temp += 1
                        # else:
                        #     temp += helper(layer - 1, i)

                        temp += helper(layer - 1, i)

                else:
                    break

            return temp

        result = 0
        for temp in tails:
            result += helper(max_seq_len - 1, temp)

        return result

# @lc code=end
