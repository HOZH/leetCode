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
        visited = [[0 for _ in range(1 << n)] for _ in range(n)]

        for i in range(n):
            queue.append([i, shift[i]])

        step = 0

        while len(queue) > 0:
            s = len(queue)

            while s > 0:
                s -= 1
                node, state = queue.popleft()
                if state == ans:
                    return step
                if visited[node][state]:
                    continue
                visited[node][state] = 1

                for j in graph[node]:
                    queue.append([j, state | shift[j]])

            step += 1

        return -1


# @lc code=end
