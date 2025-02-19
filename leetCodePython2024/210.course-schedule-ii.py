#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        # in_degree = defaultdict(int)
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
            # in_degree[course]=0
            # in_degree[prerequisite]=0

        in_degree = {node: 0 for node in range(numCourses)}
        for node in graph:
            for neighbor in graph[node]:
                in_degree[neighbor] += 1

        # 将所有入度为 0 的节点加入队列
        queue = deque([node for node in in_degree if in_degree[node] == 0])

        topo_order = []

        while queue:
            node = queue.popleft()
            topo_order.append(node)

            # 遍历邻居并减少入度
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # 若拓扑排序的元素数量不等于图中的节点数，说明图中存在环
        if len(topo_order) != len(graph):
            return []  # 图中有环，无法进行拓扑排序

        return topo_order[::-1]
        
# @lc code=end

