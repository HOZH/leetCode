#
# @lc app=leetcode id=1678 lang=python3
#
# [1678] Goal Parser Interpretation
#

# @lc code=start
class Solution:
    def interpret(self, command: str) -> str:
        ans = ''
        i = 0
        while i <len(command):
            current_char = command[i]
            if current_char == 'G':
                ans += current_char
                i+=1
            elif current_char == '(':
                i+=1
            elif current_char == 'a':
                ans+='al'
                i+=3
            elif current_char == ')':
                ans+='o'
                i+=1
                
        return ans
        
# @lc code=end

