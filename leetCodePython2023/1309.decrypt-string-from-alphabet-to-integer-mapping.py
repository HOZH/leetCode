#
# @lc app=leetcode id=1309 lang=python3
#
# [1309] Decrypt String from Alphabet to Integer Mapping
#

# @lc code=start
class Solution:
    def freqAlphabets(self, s: str) -> str:
        dictionary = {}
        for i in range(1, 10):
            dictionary[str(i)] = chr(i + 96)
        for i in range(10, 27):
            dictionary[str(i) + '#'] = chr(i + 96)

        index = len(s) - 1
        result = ''
        while index >= 0:
            current = s[index]
            if current == '#':
                result = dictionary[s[index - 2:index + 1]] + result
                index -= 3
            else:
                result = dictionary[current] + result
                index -= 1

        return result


# @lc code=end
