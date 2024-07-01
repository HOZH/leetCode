#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = dict()
        copied_nums = nums[:]
        copied_nums.sort()
        for i in range(len(nums)):
            if copied_nums[i] not in counts:
                counts[copied_nums[i]] = i

        ans = []
        for i in nums:
            ans.append(counts[i])

        return ans

        # dp = [0]*101
        # for i in nums:
        #     for j in range(i+1,101):
        #         dp[j]+=1

        # ans = []
        # for i in nums:
        #     ans.append(dp[i])

        # return ans

# @lc code=end
