#
# @lc app=leetcode id=2894 lang=python3
#
# [2894] Divisible and Non-divisible Sums Difference
#

# @lc code=start
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n/2*(1+n)
        temp = 0
        for i in range(1,n+1):
            if i%m==0:
                temp+=i
        return int(total-temp-temp)
        
        
# @lc code=end

