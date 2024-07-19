#
# @lc app=leetcode id=1859 lang=python3
#
# [1859] Sorting the Sentence
#

# @lc code=start
class Solution:
    def sortSentence(self, s: str) -> str:
        words = {}
        for i in s.split(' '):
            word, index = i[:-1], i[-1]
            words[index] = word

        ans = ''
        for i in range(1, 10):
            key = str(i)
            if key in words:
                ans += words[key]+' '

        if len(ans) != 0:
            return ans[:-1]


# @lc code=end
