#
# @lc app=leetcode id=1967 lang=python3
#
# [1967] Number of Strings That Appear as Substrings in Word
#

# @lc code=start
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return len(list(filter(lambda x: x in word, patterns)))


# @lc code=end
