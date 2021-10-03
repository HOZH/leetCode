#
# @lc app=leetcode id=1935 lang=python3
#
# [1935] Maximum Number of Words You Can Type
#

# @lc code=start
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        brokenLetters = set([*brokenLetters])

        broken_count = 0
        for current_word in text.split(' '):
            for ch in current_word:
                if ch in brokenLetters:
                    broken_count += 1
                    break

        return len(text.split(' '))-broken_count


# @lc code=end
