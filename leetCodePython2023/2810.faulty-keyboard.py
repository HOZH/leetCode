#
# @lc app=leetcode id=2810 lang=python3
#
# [2810] Faulty Keyboard
#

# @lc code=start
class Solution:
    def finalString(self, s: str) -> str:

        current = ''
        for i in s:
            if i == 'i':
                current = current[::-1]
            else:
                current += i

        return current

# @lc code=end
