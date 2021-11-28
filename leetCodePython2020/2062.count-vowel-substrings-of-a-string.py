#
# @lc app=leetcode id=2062 lang=python3
#
# [2062] Count Vowel Substrings of a String
#

# @lc code=start
from collections import Counter


class Solution:
    def countVowelSubstrings(self, word: str) -> int:

        def helper(s):
            current_counter = Counter(s)
            result = 1 if len(current_counter.keys()) == 5 else 0
            for i in range(len(s)):
                temp = s[i]
                if current_counter[temp] == 1:
                    del current_counter[temp]
                else:
                    current_counter[temp] -= 1
                if len(current_counter.keys()) == 5:
                    result += 1
                else:
                    break

            return result

        current_sub = ''
        aeiou = set(['a', 'e', 'i', 'o', 'u'])
        ans = 0

        for i in range(len(word)):
            current = word[i]
            if current in aeiou:
                current_sub += current
                ans += helper(current_sub)
            else:
                current_sub = ''

        return ans


# @lc code=end
