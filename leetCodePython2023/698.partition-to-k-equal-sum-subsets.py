#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#

# @lc code=start
from functools import lru_cache


class Solution:

    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)
        if total % k != 0:
            return False

        self.partial_sum = total//k
        nums = sorted(nums)

        if nums[-1] > self.partial_sum:
            return False

        def recurse(index, subsets):
            if index < 0:
                return True
            tried = set()

            for i in range(len(subsets)):
                if subsets[i] in tried:
                    continue
                if subsets[i]+nums[index] <= self.partial_sum:
                    subsets[i] += nums[index]

                    if recurse(index-1, subsets):
                        return True

                    subsets[i] -= nums[index]

                tried.add(subsets[i])

            return False

        return recurse(len(nums)-1, [0]*k)

    def canPartitionKSubsets_temp(self, nums: List[int], k: int) -> bool:

        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        if max(nums) > target:
            return False

        @lru_cache(None)
        def helper(current_sum, not_used, completed_count):

            if current_sum > target:
                return False
            if current_sum == target:
                completed_count += 1
                if completed_count == k:
                    return True
                flag = helper(0, not_used, completed_count)
                if flag:
                    return True

            if not_used == 0:
                return False

            for i in range(len(nums)):
                if not_used & (2 ** i):
                    flag = helper(
                        current_sum + nums[i], not_used - (2 ** i), completed_count)
                    if flag:
                        return True
            return False

        return helper(0, 2 ** (len(nums)) - 1, 0)

# @lc code=end
