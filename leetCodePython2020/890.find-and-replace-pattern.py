#
# @lc app=leetcode id=890 lang=python3
#
# [890] Find and Replace Pattern
#

# @lc code=start
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        rep = []

        for word in words+[pattern]:

            current_char = 97
            current = 'a'

            prev = ord(word[0])
            temp_dict = {word[0]: 'a'}

            for char in word[1:]:

                if char in temp_dict:
                    current += temp_dict[char]
                    prev = ord(char)

                else:
                    if ord(char) != prev:
                        current_char += 1
                        prev = ord(char)
                    temp_dict[char] = chr(current_char)
                    current += chr(current_char)

            rep.append(current)

        converted_pattern = rep[-1]
        rep = rep[:-1]

        indexes = []

        for i in range(len(rep)):
            if rep[i] == converted_pattern:

                indexes.append(i)

        return list(map(lambda x: words[x], indexes))


# @lc code=end
