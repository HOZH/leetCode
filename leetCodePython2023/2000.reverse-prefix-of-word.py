#
# @lc app=leetcode id=2000 lang=python3
#
# [2000] Reverse Prefix of Word
#

# @lc code=start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        temp = ''
        for i in range(len(word)):
            temp += word[i]
            if word[i] == ch:
                return temp[::-1]+word[i+1:]

        return temp


# @lc code=end
