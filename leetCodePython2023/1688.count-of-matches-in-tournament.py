#
# @lc app=leetcode id=1688 lang=python3
#
# [1688] Count of Matches in Tournament
#

# @lc code=start
class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n > 1:
            ans += n//2
            if n % 2 == 0:
                n //= 2
            else:
                n = n//2+1

        return ans

# @lc code=end
