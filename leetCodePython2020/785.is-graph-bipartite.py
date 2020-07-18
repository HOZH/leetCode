#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start

from collections import defaultdict, deque

# need to consider disconnected graph


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        if len(graph) == 0:
            return True

        # if all(len(i) == 0 for i in graph):
        #     return True

        # construct adjacency lists

        # g = defaultdict(list)

        # for i in range(len(graph)):
        #     g[i].extend(graph[i])

        colors = [0]*len(graph)
        # bfs

        # pick arbitrary starting point

        for i in range(len(graph)):

            if colors[i] == 0 and len(graph[i]) != 0:
                temp = graph[i][0]
            else:
                continue
                temp = None

            queue = deque()
            if temp is not None:
                queue.append(temp)
            else:
                continue
            color = 1

            current_layer = 1

            while len(queue) > 0:

                if current_layer == 0:
                    current_layer = len(queue)
                    color = 2 if (color == 1) else 1

                current = queue.popleft()
                # print(current)
                colors[current] = color

                # for i in g[current]:
                for i in graph[current]:

                    if colors[i] == 0:
                        queue.append(i)

                    elif colors[i] == color:

                        return False

                current_layer -= 1
        return True


# @lc code=end
