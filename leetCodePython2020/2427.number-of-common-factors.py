#
# @lc app=leetcode id=2427 lang=python3
#
# [2427] Number of Common Factors
#

# @lc code=start
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        for i in range(min(a, b), 0, -1):
            if a % i == 0 and b % i == 0:
                count += 1

        return count


# @lc code=end
