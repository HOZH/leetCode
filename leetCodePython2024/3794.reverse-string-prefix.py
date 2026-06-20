#
# @lc app=leetcode id=3794 lang=python3
#
# [3794] Reverse String Prefix
#

# @lc code=start
class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        return s[:k][::-1]+s[k:]

# @lc code=end
