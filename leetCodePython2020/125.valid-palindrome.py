#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ''.join(list(filter(lambda x: x.isalnum(), s))).lower()
        return temp == temp[::-1]


# @lc code=end
