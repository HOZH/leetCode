#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#

# @lc code=start
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
        
# @lc code=end

