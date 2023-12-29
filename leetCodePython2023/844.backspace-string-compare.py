#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def helper(string):
            chars = []
            for i in range(len(string)):
                if string[i] != '#':
                    chars.append(string[i])
                else:
                    chars = chars[:-1]

            return ''.join(chars)

        return helper(s) == helper(t)
# @lc code=end
