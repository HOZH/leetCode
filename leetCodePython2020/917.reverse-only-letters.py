#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:

        letters = []
        new_s = []
        for i in S:

            if i.isalpha():
                letters.append(i)
                new_s.append('a')

            else:
                new_s.append(i)

        letters = letters[::-1]

        ans = ''

        for i in range(len(new_s)):

            if new_s[i] == 'a':
                ans += letters[0]
                letters = letters[1:]
            else:
                ans += new_s[i]

        return ans


# @lc code=end
