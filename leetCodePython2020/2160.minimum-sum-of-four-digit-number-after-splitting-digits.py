#
# @lc app=leetcode id=2160 lang=python3
#
# [2160] Minimum Sum of Four Digit Number After Splitting Digits
#

# @lc code=start
class Solution:
    def minimumSum(self, num: int) -> int:
        temp = sorted([*str(num)])
        return (int(temp[0])+int(temp[1]))*10+int(temp[2])+int(temp[3])
        
# @lc code=end

