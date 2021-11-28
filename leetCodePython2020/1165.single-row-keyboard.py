#
# @lc app=leetcode id=1165 lang=python3
#
# [1165] Single-Row Keyboard
#

# @lc code=start
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        mapping = dict()
        for i in range(26):
            mapping[keyboard[i]] = i

        current, next_one = 0, 0
        ans = 0

        for i in word:
            next_one = mapping[i]
            ans += abs(next_one-current)
            current = next_one
            
        return ans

# @lc code=end
