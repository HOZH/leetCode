#
# @lc app=leetcode id=1309 lang=python3
#
# [1309] Decrypt String from Alphabet to Integer Mapping
#

# @lc code=start


class Solution:
    def freqAlphabets(self, s: str) -> str:

        mapping = dict()
        for i in range(49, 58):
            mapping[chr(i)] = chr(97+i-49)

        for i in range(10, 27):
            mapping[str(i)+'#'] = chr(106+i-10)

        temp = ''
        result = ''
        for i in range(len(s)):

            temp += s[i]
            if s[i] == '#':
                for j in range(len(temp)-3):
                    result += mapping[temp[j]]

                result += mapping[temp[-3:]]
                temp = ''
        for j in temp:
            result += mapping[j]
        return result

# @lc code=end
