#
# @lc app=leetcode id=2194 lang=python3
#
# [2194] Cells in a Range on an Excel Sheet
#

# @lc code=start
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        first, second = s.split(':')
        ans = []
        for i in range(ord(first[0]), ord(second[0])+1):
            for j in range(ord(first[1]), ord(second[1])+1):
                ans.append(chr(i)+chr(j))

        return ans


# @lc code=end
