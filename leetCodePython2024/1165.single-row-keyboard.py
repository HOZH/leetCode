#
# @lc app=leetcode id=1165 lang=python3
#
# [1165] Single-Row Keyboard
#

# @lc code=start
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyboard_mapping = {char: index for index, char in enumerate(keyboard)}

        current_index = 0
        ans = 0
        for i in word:
            ans += abs(keyboard_mapping[i]-current_index)
            current_index = keyboard_mapping[i]

        return ans


# @lc code=end
