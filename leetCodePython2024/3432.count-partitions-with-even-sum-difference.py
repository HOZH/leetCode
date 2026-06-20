#
# @lc app=leetcode id=3432 lang=python3
#
# [3432] Count Partitions with Even Sum Difference
#

# @lc code=start
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        """
        left_sum - right_sum
        = left_sum - (total_sum - left_sum)
        = 2 * left_sum - total_sum
        """
        return len(nums) - 1 if sum(nums) % 2 == 0 else 0

        left_sum, right_sum = 0, sum(nums)
        ans = 0
        for i in range(len(nums)-1):
            current = nums[i]
            left_sum += current
            right_sum -= current
            ans += 1 if ((left_sum-right_sum) % 2 == 0) else 0

        return ans


# @lc code=end
