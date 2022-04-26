#
# @lc app=leetcode id=2194 lang=python3
#
# [2194] Cells in a Range on an Excel Sheet
#

# @lc code=start
class Solution:
    def cellsInRange(self, s: str) -> List[str]:

        head,tail = s.split(":")
        head_row,head_col = ord(head[0]),int(head[1])
        tail_row,tail_col = ord(tail[0]),int(tail[1])

        result = []
        for i in range(head_row,tail_row+1):
            for j in range(head_col,tail_col+1):
                result.append(chr(i)+str(j))
        return result
        
        
# @lc code=end

