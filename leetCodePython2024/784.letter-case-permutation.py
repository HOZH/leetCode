#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        self.ans = []

        def helper(index, current_str):
            if index == len(s):
                self.ans.append(current_str)
                return

            if s[index].isalpha():
                helper(index+1, current_str+s[index].lower())
                helper(index+1, current_str+s[index].upper())
            else:
                helper(index+1, current_str+s[index])

        helper(0,'')
        return self.ans
        
# @lc code=end

