#
# @lc app=leetcode id=1925 lang=python3
#
# [1925] Count Square Sum Triples
#

# @lc code=start
class Solution:
    def countTriples(self, n: int) -> int:

        ans = 0
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                temp = i**2+j**2
                sub = int(temp**0.5)
                if sub**2 == temp and sub <= n:
                    ans += 2

        return ans


# @lc code=end
