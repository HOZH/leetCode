#
# @lc app=leetcode id=1664 lang=python3
#
# [1664] Ways to Make a Fair Array
#

# @lc code=start
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        # Calculate prefix sums for odd and even indices
        prefix_odd = [0] * (n + 1)
        prefix_even = [0] * (n + 1)
        
        for i in range(n):
            prefix_odd[i + 1] = prefix_odd[i]
            prefix_even[i + 1] = prefix_even[i]
            if i % 2 == 0:
                prefix_even[i + 1] += nums[i]
            else:
                prefix_odd[i + 1] += nums[i]

        ans = 0
        for i in range(n):
            even_sum = prefix_even[i] + (prefix_odd[n] - prefix_odd[i + 1])
            odd_sum = prefix_odd[i] + (prefix_even[n] - prefix_even[i + 1])
            if even_sum == odd_sum:
                ans += 1

        return ans
        
# @lc code=end

