#
# @lc app=leetcode id=2427 lang=python3
#
# [2427] Number of Common Factors
#

# @lc code=start
class Solution:
    def commonFactors(self, a: int, b: int) -> int:

        up_bound = min(a, b)
        result = 0
        for i in range(1, up_bound+1):
            if a % i == 0 and b % i == 0:
                result += 1

        return result


# @lc code=end
