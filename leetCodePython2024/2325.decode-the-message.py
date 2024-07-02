#
# @lc app=leetcode id=2325 lang=python3
#
# [2325] Decode the Message
#

# @lc code=start
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dictionary = {}
        current_index = 0
        for i in key:
            if i not in dictionary and i != ' ':
                dictionary[i] = current_index
                current_index += 1
        ans = ''
        for i in message:
            if i == ' ':
                ans += ' '
            else:
                ans += chr(97+dictionary[i])

        return ans


# @lc code=end
