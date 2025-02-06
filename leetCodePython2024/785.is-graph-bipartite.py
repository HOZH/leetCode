#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        if len(graph) < 3:
            return True
        colors = [0] * len(graph)

        # 2023 revision
        for i in range(len(graph)):
            if colors[i] == 0:
                if not len(graph[i]):
                    continue
                else:
                    queue = deque([i])
                    color = 1
                    colors[i] = color
                    while len(queue):
                        current_layer_len = len(queue)
                        color = 2 if color == 1 else 1
                        while current_layer_len:
                            current = queue.popleft()
                            current_layer_len -= 1
                            for j in graph[current]:
                                if colors[j] == 0:
                                    colors[j] = color
                                    queue.append(j)
                                else:
                                    if colors[j] != color:
                                        return False
            else:
                continue
        return True


# @lc code=end
