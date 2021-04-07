#
# @lc app=leetcode id=847 lang=python3
#
# [847] Shortest Path Visiting All Nodes
#

# @lc code=start

from collections import deque


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        shift = [1 << i for i in range(n)]
        ans = (1 << n)-1
        queue = deque()

        # [i][j], i->current node, j->current state. visited's used to check if a state with i as last step has been encoutered b4
        visited = [[0 for _ in range(1 << n)] for _ in range(n)]

        for i in range(n):
            # append all the node to queue with inital state which a node only vesited it self
            queue.append([i, shift[i]])

        step = 0

        while len(queue):
            # get length for current layer in bfs
            s = len(queue)

            while s:
                s -= 1
                node, state = queue.popleft()
                if state == ans:
                    return step
                if visited[node][state]:
                    continue
                visited[node][state] = 1

                # add adjacent nodes with updated state
                # will only be operated after current logic layer (bfs)
                for j in graph[node]:
                    queue.append([j, state | shift[j]])
            step += 1

        return -1
# @lc code=end
