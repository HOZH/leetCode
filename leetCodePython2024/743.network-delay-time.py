#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    
        graph = defaultdict(list)
        for start, end, weight in times:
            graph[start].append((end, weight))

        distances = {i: float('inf') for i in range(1, n + 1)}
        distances[k] = 0
        queue = [(0, k)]

        while queue:
            current_dis, current_node = heappop(queue)
            if current_dis > distances[current_node]:
                continue            
            for neighbor, weight in graph[current_node]:
                distance = current_dis + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heappush(queue, (distance, neighbor))

        max_distance = max(distances.values())
        return max_distance if max_distance < float('inf') else -1

# @lc code=end

