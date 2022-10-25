#
# @lc app=leetcode id=2255 lang=python3
#
# [2255] Count Prefixes of a Given String
#

# @lc code=start
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for i in words:
            if s.startswith(i):
                count += 1
        return count

# @lc code=end
