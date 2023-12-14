#
# @lc app=leetcode id=2194 lang=python3
#
# [2194] Cells in a Range on an Excel Sheet
#

# @lc code=start
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        temp = s.split(':')
        head_row, head_col = temp[0]
        tail_row, tail_col = temp[1]

        head_row_num, tail_row_num = ord(head_row), ord(tail_row)
        head_col_num, tail_col_num = int(head_col), int(tail_col)
        ans = []

        for i in range(head_row_num, tail_row_num+1):

            for j in range(int(head_col_num), int(tail_col_num)+1):
                ans.append(chr(i)+str(j))

        return ans

# @lc code=end
