#
# @lc app=leetcode id=709 lang=python3
#
# [709] To Lower Case
#

# @lc code=start


class Solution:
    def toLowerCase(self, str: str) -> str:

        return ''.join(list(map(lambda x: chr(ord(x)+32) if ord(x) in range(65, 91) else x, list(str))))

# @lc code=end
