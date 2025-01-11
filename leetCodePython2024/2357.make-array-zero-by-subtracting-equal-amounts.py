#
# @lc app=leetcode id=2357 lang=python3
#
# [2357] Make Array Zero by Subtracting Equal Amounts
#

# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums) - {0})
        if all([i == 0 for i in nums]):
            return 0
        ans = 0
        nums = list(filter(lambda x: x != 0, nums))
        while len(nums) and max(nums) > 0:
            min_val = min(nums)
            nums = list(
                filter(lambda y: y > 0, map(lambda x: x-min_val, nums)))
            ans += 1
        return ans


# @lc code=end
