#
# @lc app=leetcode id=824 lang=python3
#
# [824] Goat Latin
#

# @lc code=start
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(' ')
        ans_list = []
        for i in range(len(words)):
            current = words[i]
            if current[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                ans_list.append(current+'ma'+'a'*(i+1))
            else:
                ans_list.append(current[1:]+current[0]+'ma'+'a'*(i+1))

        return ' '.join(ans_list)

# @lc code=end
