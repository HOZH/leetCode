#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
#

# @lc code=start
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digs = list(filter(lambda x: x.split(' ')[1].isdecimal(), logs))
        lets = sorted(list(filter(lambda x: x.split(
            ' ')[1].isalpha(), logs)), key=lambda x: (' '.join(x.split(' ')[1:]), x.split(' ')[0]))

        return lets+digs
# @lc code=end
