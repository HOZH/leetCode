#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#

# @lc code=start
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        chars_in_words = list(map(lambda x: set([*x]), words))
        if not len(chars_in_words):
            return []
        common_chars = chars_in_words[0]
        for i in range(1, len(chars_in_words)):
            common_chars &= chars_in_words[i]

        ans = []
        common_chars = list(common_chars)
        common_chars.sort()
        for i in common_chars:
            char_count = 10e5
            for j in words:
                char_count = min(j.count(i), char_count)

            ans.extend([i]*char_count)

        return ans


# @lc code=end
