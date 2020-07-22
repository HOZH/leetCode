#
# @lc app=leetcode id=1192 lang=python3
#
# [1192] Critical Connections in a Network
#

# @lc code=start


class Solution:
    def criticalConnections(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ids, low = [-1] * n, [0] * n
        id_max, bridges = 0, []

        def dfs(u, parent, bridges):
            nonlocal id_max
            id_max += 1
            ids[u] = low[u] = id_max

            for v in graph[u]:
                if v == parent:
                    continue
                if ids[v] == -1:
                    dfs(v, u, bridges)
                    low[u] = min(low[u], low[v])
                    if ids[u] < low[v]:
                        bridges.append([u, v])
                else:
                    low[u] = min(low[u], ids[v])
        dfs(u, -1, bridges)
        return bridges

# @lc code=end
