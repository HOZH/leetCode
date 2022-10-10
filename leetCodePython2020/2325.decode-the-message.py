#
# @lc app=leetcode id=2325 lang=python3
#
# [2325] Decode the Message
#

# @lc code=start
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {' ': ' '}
        i = 0
        res = ''
        letters = [ chr(i) for i in range(97,123)]
        for char in key:
            if char not in mapping:
                mapping[char] = letters[i]
                i += 1
        for char in message:
            res += mapping[char]
        return res


# @lc code=end
