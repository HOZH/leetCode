
from functools import reduce
a= int(reduce(lambda x, y: int(x)+int(y), [1,1,3]))
print(a)


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        if not len(costs):
            return 0

        dp = [[0, 0, 0] for _ in range(len(costs))]

        dp[0] = costs[0][:]

        for i in range(1, len(costs)):
            prev_red, prev_blue, prev_green = dp[i -
                                                 1][0], dp[i-1][1], dp[i-1][2]

            dp[i][0] = costs[i][0]+min(prev_blue, prev_green)
            dp[i][1] = costs[i][1]+min(prev_red, prev_green)
            dp[i][2] = costs[i][2]+min(prev_red, prev_blue)

        return min(dp[-1])


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        for i in range(1, len(costs)):
            costs[i][0] += min(costs[i-1][1], costs[i-1][2])
            costs[i][1] += min(costs[i-1][0], costs[i-1][2])
            costs[i][2] += min(costs[i-1][0], costs[i-1][1])
        return min(costs[-1])