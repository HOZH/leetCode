#
# @lc app=leetcode id=1945 lang=python3
#
# [1945] Sum of Digits of String After Convert
#

# @lc code=start
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_str = ''
        for i in s:
            num_str += str(ord(i)-96)
        for i in range(k):
            temp = 0
            for j in num_str:
                temp += int(j)
            num_str = str(temp)

        return int(num_str)

# @lc code=end
