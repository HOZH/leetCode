#
# @lc app=leetcode id=1119 lang=python3
#
# [1119] Remove Vowels from a String
#

# @lc code=start
class Solution:
    def removeVowels(self, s: str) -> str:
        not_valid = {'a', 'e', 'i', 'o', 'u'}
        return ''.join(list(filter(lambda x: x not in not_valid, s)))

# @lc code=end
