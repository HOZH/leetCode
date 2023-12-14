
# Roses    1   2    3   4    5
# Profit  $5  $13  $24 $30  $35
remaining_count = 9
for i in range(1, min(remaining_count+1, 6)):
    print(i,remaining_count-i)

for i in range(5,0,-1):
    print(i)
class Solution:

    def __init__(self):
        self.base = [0, 5, 13, 24, 30, 35]

    def solve_with_recursion(self, remaining_count):
        if remaining_count <= 5:
            return self.base[remaining_count]
        local_max = float('-inf')

        for i in range(1, min(remaining_count + 1, 6)):
            local_max = max(
                local_max, self.base[i]+self.solution_using_recursion(remaining_count-i))
        return local_max
    def solve_with_dp(self, count):
        dp = [0]*(count+1)
        for i in range(1,6):
            dp[i]=self.base[i]
        
        for i in range(6,len(dp)):
            for j in range(min(5,i-1),0):
                dp[i]=max(dp[i-j]+dp[j])

        return dp[-1]


print(Solution().solution_using_recursion(15))
