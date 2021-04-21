#
# @lc app=leetcode id=824 lang=python3
#
# [824] Goat Latin
#

# @lc code=start
class Solution:
    def toGoatLatin(self, S: str) -> str:

        words = S.split(' ')
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        for i in range(len(words)):

            current = words[i]

            if current[0] in vowels:
                words[i] = words[i]+'ma'
            else:
                words[i] = words[i][1:]+words[i][0]+'ma'

            words[i] += 'a'*(i+1)

        return ' '.join(words)


# @lc code=end
