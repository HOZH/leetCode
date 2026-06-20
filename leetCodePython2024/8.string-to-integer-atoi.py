#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        # skip leading whitespace
        s= s.lstrip()
        sign = None
        if not len(s):
            return 0
        if s[0] in ['-','+']:
            sign = s[0]
            s = s[1:]
        
        abs_ans = 0
        is_leading_zero = True
        for char in s:
            if not char.isdigit():
                break
            if is_leading_zero and char == '0':
                continue
            else:
                is_leading_zero = False
                abs_ans = abs_ans*10 + int(char)
        
        if sign == None or sign == '+':
            return min(abs_ans, 2**31 -1)
        else:
            return max(-abs_ans, -2**31)

        
# @lc code=end

