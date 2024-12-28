#
# @lc app=leetcode id=2367 lang=python3
#
# [2367] Number of Arithmetic Triplets
#

# @lc code=start
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                if nums[j] - nums[i] == diff:
                    for k in range(j+1, length):
                        if nums[k] - nums[j] == diff:
                            ans += 1

        return ans

# @lc code=end
