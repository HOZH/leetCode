#
# @lc app=leetcode id=2315 lang=python3
#
# [2315] Count Asterisks
#

# @lc code=start
class Solution:
    def countAsterisks(self, s: str) -> int:
        temp = s.split('|')
        placeholder = ''
        for i in range(len(temp)):
            if i % 2 == 0:
                placeholder += temp[i]

        return placeholder.count('*')


# @lc code=end
