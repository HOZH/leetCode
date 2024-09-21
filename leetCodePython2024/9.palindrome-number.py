#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_rep = str(x)
        return str_rep == str_rep[::-1]

# @lc code=end
