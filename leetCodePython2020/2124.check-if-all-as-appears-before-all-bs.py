#
# @lc app=leetcode id=2124 lang=python3
#
# [2124] Check if All A's Appears Before All B's
#

# @lc code=start
class Solution:
    def checkString(self, s: str) -> bool:

        temp = -1
        for i in range(len(s)):
            if s[i] != 'a':
                temp = i
                break

        if temp == -1:
            return True

        for i in range(temp+1, len(s)):
            if s[i] == 'a':
                return False
        return True

# @lc code=end
