#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(arr):

            if len(arr) == 0:
                return 0
            if len(arr) == 1:
                return arr[0]

            dp = [0 for _ in range(len(arr))]
            dp[0] = arr[0]
            dp[1] = arr[0] if arr[0] > arr[1] else arr[1]

            for i in range(2, len(arr)):
                dp[i] = max(dp[i-2]+arr[i], dp[i-1])

            return dp[-1]

        # case 1, using 0 -> 0~n-1
        first = helper(nums[:-1])
        # case 2, using 1 -> 1~n
        second = helper(nums[1:])

        return max(first, second)


# @lc code=end
