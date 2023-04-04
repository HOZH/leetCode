#
# @lc app=leetcode id=1165 lang=python3
#
# [1165] Single-Row Keyboard
#

# @lc code=start
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        mapping = {}
        for i in range(len(keyboard)):
            mapping[keyboard[i]] = i
        index = 0
        ans = 0

        for i in range(len(word)):
            current = mapping[word[i]]
            ans += abs(current-index)
            index = current

        return ans


# @lc code=end
