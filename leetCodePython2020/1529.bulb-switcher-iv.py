#
# @lc app=leetcode id=1529 lang=python3
#
# [1529] Bulb Switcher IV
#

# @lc code=start
class Solution:
    def minFlips(self, target: str) -> int:

        result = 0
        current = 0

        for i in target:
            if ord(i) - 48 != current:
                current = 1 ^ current
                result += 1

        return result


# @lc code=end
