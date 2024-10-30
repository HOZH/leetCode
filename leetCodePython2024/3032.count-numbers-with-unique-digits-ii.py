#
# @lc app=leetcode id=3032 lang=python3
#
# [3032] Count Numbers With Unique Digits II
#

# @lc code=start
class Solution:
    def numberCount(self, a: int, b: int) -> int:
        ans = 0
        for i in range(a, b+1):
            if len(set([*str(i)])) == len(str(i)):
                ans += 1
        return ans

# @lc code=end
