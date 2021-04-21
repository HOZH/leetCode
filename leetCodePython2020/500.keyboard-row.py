#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        first = set([*"qwertyuiop"])
        sec = set([*"asdfghjkl"])
        third = set([*"zxcvbnm"])

        ans = []

        for i in words:
            temp = [*i.lower()]
            if all([j in first for j in temp]) or all([j in sec for j in temp]) or all([j in third for j in temp]):
                ans.append(i)

        return ans


# @lc code=end
