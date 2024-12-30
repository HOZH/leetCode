#
# @lc app=leetcode id=2109 lang=python3
#
# [2109] Adding Spaces to a String
#

# @lc code=start
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        if not len(s):
            return ''
        prev = 0
        words = []
        for i in spaces:
            words.append(s[prev:i])
            prev = i
        words.append(s[prev:])

        return ' '.join(words)


# @lc code=end
