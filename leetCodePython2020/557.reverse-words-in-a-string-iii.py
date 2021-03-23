#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split(' ')

        words = list(map(lambda x: x[::-1], words))

        return ' '.join(words)

# @lc code=end
