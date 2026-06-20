#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        str_representation = str(x)
        has_negative_sign = str_representation[0] == '-'
        if has_negative_sign:
            str_representation = str_representation[1:]
        reversed_str = str_representation[::-1]
        if has_negative_sign:
            reversed_str = '-' + reversed_str
        ans = int(reversed_str)
        if ans < -2**31 or ans > 2**31 - 1:
            return 0
        
        return ans            
        
# @lc code=end

