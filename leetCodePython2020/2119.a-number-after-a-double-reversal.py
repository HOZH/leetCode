#
# @lc app=leetcode id=2119 lang=python3
#
# [2119] A Number After a Double Reversal
#

# @lc code=start
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        temp = str(num)[::-1]
        while len(temp):
            if temp[0] == '0':
                temp = temp[1:]
            else:
                break

        temp = temp[::-1]

        while len(temp):
            if temp[0] == '0':
                temp = temp[1:]
            else:
                break
        if not len(temp):
            return False

        return int(temp) == num


# @lc code=end
