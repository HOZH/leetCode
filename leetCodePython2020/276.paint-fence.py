#
# @lc app=leetcode id=276 lang=python3
#
# [276] Paint Fence
#

# @lc code=start
class Solution:
    def numWays(self, n: int, k: int) -> int:

        if n==1:
            return k
        if n==2:
            return k**2

        prev_one,prev_two = k**2,k
        for _ in range(2,n):
            temp = (k-1)*(prev_one+prev_two)
            prev_two=prev_one
            prev_one=temp
            
        return prev_one

    def numWays_temp(self, n: int, k: int) -> int:

        if n==1:
            return k
        if n==2:
            return k**2


        dp = [[ 0 for _ in range(k) ] for _ in range(n)]
        for i in range(k):
            dp[0][i]=1
            dp[1][i]=k

        
        for day in range(2,n):
            for color in range(k):
                temp1 = sum(dp[day-1])-dp[day-1][color] # diff color previous one
                temp2 = (sum(dp[day-2])-dp[day-2][color]) # same color previous one but diff color previous two
                dp[day][color]=temp1 + temp2
        
        return sum(dp[-1])

        
        
# @lc code=end

