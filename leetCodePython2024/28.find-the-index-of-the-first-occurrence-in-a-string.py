#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
# haystack = "leetcoleetode", 
# haystack = "l  e   l eetocoleetde", # [0, ]
# lllleeto

# needle = "lee  to"
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

# @lc code=end
