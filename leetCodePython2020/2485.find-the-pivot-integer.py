#
# @lc app=leetcode id=2485 lang=python3
#
# [2485] Find the Pivot Integer
#

# @lc code=start
class Solution:
    def pivotInteger(self, n: int) -> int:
        target = n*(n+1)/2/2
        
        l,r = 1,n
        while l < r:
            m = l+(r-l)//2
            if m*(m+1)/2 >= n*(n+1)/2/2:
                r = m
            else:
                l = m+1

        if l*(l+1)/2-l/2==target:
            return l
        return -1
            
        
            
        
# @lc code=end

