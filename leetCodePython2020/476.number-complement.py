#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        temp = "{0:b}".format(num)
        return int(''.join(list(map(lambda x: '1' if x == '0' else '0', temp))), 2)


# @lc code=end
