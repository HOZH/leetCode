#
# @lc app=leetcode id=1323 lang=python3
#
# [1323] Maximum 69 Number
#

# @lc code=start


class Solution:
    def maximum69Number(self, num: int) -> int:

        s = list(str(num))

        for i in range(len(s)):
            if s[i] == '6':
                s[i] = '9'
                return int(''.join(s))

        return num

# @lc code=end
