#
# @lc app=leetcode id=3280 lang=python3
#
# [3280] Convert Date to Binary
#

# @lc code=start
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date_divided_by_unit = date.split('-')
        ans = ''
        for i in date_divided_by_unit:
            ans += '{0:b}'.format(int(i))+'-'

        return ans[:-1]

# @lc code=end
