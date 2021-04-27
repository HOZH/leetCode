#
# @lc app=leetcode id=806 lang=python3
#
# [806] Number of Lines To Write String
#

# @lc code=start
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:

        lines, last_line_width = 0, 0

        current_width = 0

        for i in s:
            i_width = widths[ord(i)-97]
            if current_width + i_width <= 100:
                current_width += i_width
            else:
                current_width = i_width
                lines += 1

        last_line_width = current_width
        lines += 1 if(lines != 0 or last_line_width != 0) else 0

        return [lines, last_line_width]

# @lc code=end
