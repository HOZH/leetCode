#
# @lc app=leetcode id=1374 lang=python3
#
# [1374] Generate a String With Characters That Have Odd Counts
#

# @lc code=start


class Solution:
    def generateTheString(self, n: int) -> str:

        return 'a'*(n-1)+'b' if n % 2 == 0 else 'a'*n


# @lc code=end
