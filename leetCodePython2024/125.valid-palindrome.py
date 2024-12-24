#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_str = ''.join(list(filter(lambda x: (
            96 < ord(x.lower()) < 123) or (47 < ord(x.lower()) < 58), s))).lower()
        return filtered_str == filtered_str[::-1]

# @lc code=end
