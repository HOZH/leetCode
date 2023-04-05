#
# @lc app=leetcode id=1323 lang=python3
#
# [1323] Maximum 69 Number
#

# @lc code=start
class Solution:
    def maximum69Number(self, num: int) -> int:
        temp = [*str(num)]
        for i in range(len(temp)):
            if temp[i] == '6':
                temp[i] = '9'
                break
        return int(''.join(temp))

# @lc code=end
