#
# @lc app=leetcode id=1085 lang=python3
#
# [1085] Sum of Digits in the Minimum Number
#

# @lc code=start
class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:

        nums.sort()
        current = str(nums[0])

        ans = 0
        for i in current:
            ans += int(i)

        return 0 if ans % 2 == 1 else 1

# @lc code=end
