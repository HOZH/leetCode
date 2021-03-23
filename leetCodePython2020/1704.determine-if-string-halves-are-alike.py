#
# @lc app=leetcode id=1704 lang=python3
#
# [1704] Determine if String Halves Are Alike
#

# @lc code=start
class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        half_size = len(s)//2
        first_half, sec_half = s[:half_size].lower(), s[half_size:].lower()

        first_count, sec_count = 0, 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for i in range(half_size):

            if first_half[i] in vowels:
                first_count += 1
            if sec_half[i] in vowels:
                sec_count += 1

        return first_count == sec_count


# @lc code=end
