#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(list(filter(lambda x: x != '', s.split(' ')))[-1])

# @lc code=end
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        new_s = s.rstrip()
        start_index = 0
        i = len(new_s) - 1
        while i >= 0:
            curr = new_s[i]
            if curr == " ":
                start_index = i + 1
                break
            else:
                i -= 1
        return len(new_s) - 1 - start_index