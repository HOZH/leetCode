#
# @lc app=leetcode id=3110 lang=python3
#
# [3110] Score of a String
#

# @lc code=start
class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for i in range(len(s)-1):
            ans+=abs(ord(s[i])-ord(s[i+1]))
        return ans

        
# @lc code=end

