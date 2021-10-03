#
# @lc app=leetcode id=1525 lang=python3
#
# [1525] Number of Good Ways to Split a String
#

# @lc code=start
class Solution:
    def numSplits(self, s: str) -> int:

        if not s:
            return 0

        count = 0

        first_half, sec_half = dict(), dict()

        first_half[s[0]] = 1

        for i in range(1, len(s)):
            if s[i] not in sec_half:
                sec_half[s[i]] = 0

            sec_half[s[i]] += 1

        count = 1 if len(first_half.keys()) == len(sec_half.keys()) else 0

        for i in range(1, len(s)):

            current_char = s[i]
            # process first half
            if current_char not in first_half:
                first_half[current_char] = 0
            first_half[current_char] += 1
            # process sec half

            if sec_half[current_char] == 1:
                del sec_half[current_char]
            else:
                sec_half[current_char] -= 1

            # conditionally increase count
            count += 1 if len(first_half.keys()) == len(sec_half.keys()) else 0

        return count


# @lc code=end
