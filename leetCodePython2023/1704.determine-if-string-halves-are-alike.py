#
# @lc app=leetcode id=1704 lang=python3
#
# [1704] Determine if String Halves Are Alike
#

# @lc code=start
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        first_half, sec_half = s[:len(s)//2].lower(), s[len(s)//2:].lower()

        def helper(half):
            return len(list(filter(lambda x: x in ('a', 'e', 'i', 'o', 'u'), half)))
        
        return helper(first_half) == helper(sec_half)

# @lc code=end
