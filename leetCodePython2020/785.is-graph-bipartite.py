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

        if len(graph) < 2:
            return True
        colors = [0]*len(graph)

        # bfs
        # pick arbitrary starting point

        for i in range(len(graph)):
            # color !=0 implies that we have visited current node
            if colors[i] == 0 and len(graph[i]) > 0:
                # if len(graph[i])==0 -> it's possible in undirect unconnected graph
                temp = graph[i][0]
            else:
                continue
            queue = deque()

            queue.append(temp)

            colors[temp] = 1

            while len(queue):

                current_node = queue.popleft()

                # filp current color
                color = 2 if colors[current_node] == 1 else 1

                for current_child in graph[current_node]:

                    if colors[current_child] == 0:
                        colors[current_child] = color
                        queue.append(current_child)
                    else:
                        if colors[current_child] != color:
                            return False
        return True


# @lc code=end
