#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#

# @lc code=start
class Solution:
    # def deleteAndEarn(self, nums: List[int]) -> int:
    #     if len(nums) == 0:
    #         return 0
    #     arr = [0]*(max(nums)+1)
    #     dp = arr[:]

    #     for i in nums:
    #         arr[i] += i

    #     dp[0] = arr[0]
    #     dp[1] = max(dp[0], arr[1])
    #     for i in range(2, len(dp)):
    #         dp[i] = max(dp[i-1], dp[i-2]+arr[i])

    #     return dp[-1]

    def deleteAndEarn(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        temp = max(nums)+1

        arr = [0]*(temp)
        dp = [0]*(temp)

        for i in nums:
            arr[i] += i

        dp[0] = arr[0]

        for i in range(1, temp):

            dp[i] = max(dp[i-1], arr[i] + (0 if i-1 == 0 else dp[i-2]))

        return dp[-1]


# @lc code=end
