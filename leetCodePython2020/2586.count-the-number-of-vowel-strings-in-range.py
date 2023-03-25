#
# @lc app=leetcode id=2586 lang=python3
#
# [2586] Count the Number of Vowel Strings in Range
#

# @lc code=start
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:

        ans = 0
        keys = {'a', 'e', 'i', 'o', 'u'}

        for i in range(left, min(right+1, len(words))):
            ans += 1 if (words[i][-1] in keys and words[i][0] in keys) else 0
        return ans

# @lc code=end
