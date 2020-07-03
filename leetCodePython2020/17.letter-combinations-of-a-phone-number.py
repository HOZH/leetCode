#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start

# from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        self.result = []
        self.map = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': [
            'm', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        

        def helper(arr,s):

            if len(arr)==0:
                self.result.append(s)
                return

            current_d = arr[0]

            for i in self.map[current_d]:
                helper(arr[1:],s+i)

        helper(digits,'')
        
        return list(filter(lambda x:x!='',self.result))




# @lc code=end
