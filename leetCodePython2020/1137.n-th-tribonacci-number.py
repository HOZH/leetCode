#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start


class Solution:
    def tribonacci(self, n: int) -> int:
        # lst = [0, 1, 1]
        # if n < 2:
        #     return lst[n]
        # else:            
        #     for i in range(n-2):
        #         lst.append(sum(lst))
        #         lst.pop(0)
        # return lst.pop()

        dp = [0]*(max(n, 3)+1)
        dp[1] = 1
        dp[2] = 1
        dp[3] = 2
        for i in range(4, n+1):
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
            # dp[i] = dp[i-1]*2-dp[i-4]

        return dp[n]

# @lc code=end
