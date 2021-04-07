from typing import List


class Solution:
    def criticalConnections(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for i in range(n+1)]
        ids, low = dict(), dict()

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            ids[u] = -1
            ids[v] = -1
            low[u] = 0
            low[v] = 0

        # ids, low = [-1] * (n+1), [0] * (n+1)
        # ids,low=dict(),dict()

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
                        bridges.append(sorted([u, v]))
                else:
                    low[u] = min(low[u], ids[v])
        dfs(u, -1, bridges)
        return sorted(bridges)


t = Solution()
print(t.criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]))
print(t.criticalConnections(
    6, [[1, 2], [1, 3], [2, 3], [2, 4], [2, 5], [4, 6], [5, 6]]))
print(t.criticalConnections(
    9, [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6],
        [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]]
))
