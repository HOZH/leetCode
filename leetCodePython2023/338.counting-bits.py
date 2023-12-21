#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(0, n+1):
            ans.append('{0:b}'.format(i).count('1'))
        return ans

# @lc code=end
