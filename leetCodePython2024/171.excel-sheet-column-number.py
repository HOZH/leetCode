#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        order = 0
        ans = 0
        for i in range(len(columnTitle)-1, -1, -1):
            current = ord(columnTitle[i])-64
            ans += (current*(26**order))
            ans = ans + current*(26**order)
            order += 1
        return ans




class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        i = len(columnTitle) - 1

        output = 0
        exponent_counter = 0
        while i >= 0:
            char = columnTitle[i]
            char_val = self.get_letter_value(char)
            output = output + (char_val * (26 ** exponent_counter))

            exponent_counter += 1
            i -= 1
        
        return output


    def get_letter_value(self, letter):
        return ord(letter) - 64

# bag = {chr(i): i - 64 for i in range(65, 91)}

# @lc code=end


# hex decimal A = 10
# 1,2,3,4,5,6,7,8,9,A,b,c,d

'AB'
"ZY" -> y is least significant digit,
a = 1, b = 2
we always do calculation for the least significant digit

2*26**0+1*26**1

26**0 = 1
26 ** 1 = 26
26 ** 2 = 676
