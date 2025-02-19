#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 初始化距离数组，初始时 src 到所有城市的距离为无穷大，除了自己
        dist = [float("inf")] * n
        dist[src] = 0

        # 进行 k+1 轮松弛操作
        for _ in range(k+1):
            new_dist = dist[:]  # 复制当前状态
            for u, v, price in flights:
                if dist[u] != float("inf") and dist[u] + price < new_dist[v]:
                    new_dist[v] = dist[u] + price
            dist = new_dist  # 更新状态
        # print(dist)

        return dist[dst] if dist[dst] != float("inf") else -1

# @lc code=end

