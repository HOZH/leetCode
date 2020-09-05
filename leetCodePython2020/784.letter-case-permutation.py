#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#

# @lc code=start


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:

        self.ans = []

        def helper(s, current_string: str):
            if len(s) == 0:
                self.ans.append(current_string)
                return
            current_char = ord(s[0])
            if current_char in range(48, 58):
                helper(s[1:], current_string+s[0])
            else:
                helper(s[1:], current_string+s[0].lower())
                helper(s[1:], current_string+s[0].upper())

        helper(S, '')
        return self.ans


# @lc code=end
