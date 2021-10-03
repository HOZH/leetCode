#
# @lc app=leetcode id=1910 lang=python3
#
# [1910] Remove All Occurrences of a Substring
#

# @lc code=start
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        current = s

        while part in current:
            current = current.replace(part, '', 1)

        return current

# @lc code=end
