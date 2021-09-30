#
# @lc app=leetcode id=2000 lang=python3
#
# [2000] Reverse Prefix of Word
#

# @lc code=start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        temp = word.find(ch)

        if not temp:
            return word

        return word[:temp+1][::-1]+word[temp+1:]


# @lc code=end
