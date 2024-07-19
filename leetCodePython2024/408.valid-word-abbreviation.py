#
# @lc app=leetcode id=408 lang=python3
#
# [408] Valid Word Abbreviation
#

# @lc code=start
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # processed_tokens = []
        # current_str_token = ""
        # for i in abbr:
        #     if i.isnumeric():
        #         if current_str_token.isnumeric():
        #             current_str_token += i
        #         else:
        #             if i == "0":
        #                 return False
        #             else:
        #                 current_str_token = i
        #     else:
        #         if current_str_token.isnumeric():
        #             processed_tokens.append(int(current_str_token))
        #         current_str_token = i
        #         processed_tokens.append(i)
        # if current_str_token.isnumeric():
        #     processed_tokens.append(int(current_str_token))

        # index = 0
        # while index < len(word):
        #     if len(processed_tokens) == 0:
        #         return not (index != len(word))

        #     current_token = processed_tokens[0]
        #     processed_tokens = processed_tokens[1:]

        #     if type(current_token) is not int:
        #         if current_token != word[index]:
        #             return False
        #         index += 1
        #     else:
        #         index += current_token
        # return True if (len(processed_tokens) == 0 and index <= len(word)) else False

        i, j, m, prev = len(word), len(abbr), 1, None

        while i > 0 and j > 0:
            c1, c2 = word[i-1], abbr[j-1]
            if c1 == c2:
                i -= 1
                j -= 1
                m = 1
                if prev == 0:
                    return False
            elif c2.isnumeric():
                i -= int(c2)*m
                j -= 1
                m *= 10
                prev = int(c2)
            else:
                return False

        return i == j == 0


# @lc code=end
