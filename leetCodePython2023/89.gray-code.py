#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        dp = [0]

        for i in range(n):
            dp = dp+[x | 1 << i for x in reversed(dp)]

        return dp
        
# @lc code=end

