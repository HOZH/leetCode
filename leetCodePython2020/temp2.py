

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n<3: return (0,1,1)[n]
        dp = [0]*(n+1)
        dp[1]=1
        
        for i in range(2, n+1):
            dp[i] = dp[i//2] if i%2==0 else dp[(i-1)//2]+dp[(i-1)//2+1]
        return max(dp)


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0]*(n+1)
        dp[0], dp[1] = 0, 1

        for i in range(2, n+1):
            if i % 2 == 0:
                dp[i] = dp[i//2]
            else:
                dp[i] = dp[i//2]+dp[i//2+1]
        return max(dp)
