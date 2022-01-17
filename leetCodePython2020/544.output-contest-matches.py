#
# @lc app=leetcode id=544 lang=python3
#
# [544] Output Contest Matches
#

# @lc code=start
class Solution:
    def findContestMatch(self, n: int) -> str:
        def recursion(matches, x):
            if x == 1:
                return matches[0]
            layer = x//2
            return recursion(tuple((matches[i], matches[x-i-1]) for i in range(layer)), layer)
        return str(recursion([(i+1, n-i) for i in range(n//2)], n//2)).replace(' ', '')


        
# @lc code=end

