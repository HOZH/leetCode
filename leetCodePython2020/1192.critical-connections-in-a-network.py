#
# @lc app=leetcode id=1192 lang=python3
#
# [1192] Critical Connections in a Network
#

# @lc code=start


class Solution:
    def criticalConnections(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        rank, lowest_group = [-1] * n, [0] * n
        id_max, bridges = 0, []

        def dfs(u, parent, bridges):
            nonlocal id_max
            id_max += 1

            rank[u] = id_max
            lowest_group[u] = id_max

            for v in graph[u]:
                if v == parent:
                    continue
                # v was never reached before
                if rank[v] == -1:
                    dfs(v, u, bridges)
                    # if v (u's next node can reach to lower group and u,v are connect)
                    # this means u can also reach to lower group -> implies back edge
                    # so u,v is not critical edge
                    lowest_group[u] = min(lowest_group[u], lowest_group[v])
                    # not back edge found in farther pathing, so u,v is a critical edge
                    if rank[u] < lowest_group[v]:
                        bridges.append([u, v])
                else:
                    lowest_group[u] = min(lowest_group[u], rank[v])
        dfs(u, -1, bridges)
        # return list(map(lambda x: x if x in edges else [x[1], x[0]], bridges))
        return bridges

# @lc code=end
