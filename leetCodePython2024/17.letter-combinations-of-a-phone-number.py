#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        mapping = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': [
            'm', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        self.ans = []

        def helper(remainning_input, current):
            if len(remainning_input) == 0:
                self.ans.append(current)
                return

            for i in mapping[remainning_input[0]]:
                helper(remainning_input[1:], current+i)

        helper(digits, '')

        return self.ans


# @lc code=end
