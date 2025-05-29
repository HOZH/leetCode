#
# @lc app=leetcode id=1295 lang=python3
#
# [1295] Find Numbers with Even Number of Digits
#

# @lc code=start
class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        def helper(n):
            count = 0
            while n > 0:
                count += 1
                n //= 10
            return count
        return sum(1 for i in nums if helper(i) % 2 == 0)

# @lc code=end
