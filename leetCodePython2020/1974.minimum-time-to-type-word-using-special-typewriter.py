#
# @lc app=leetcode id=1974 lang=python3
#
# [1974] Minimum Time to Type Word Using Special Typewriter
#

# @lc code=start
class Solution:
    def minTimeToType(self, word: str) -> int:

        current_location = 97
        result = 0

        for i in word:
            temp = abs(ord(i)-current_location)
            result += min(temp, 26-temp)+1
            current_location = ord(i)

        return result

# @lc code=end
