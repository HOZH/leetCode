#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
            return False  # 图中有环，无法进行拓扑排序

        return True
    
        ######
        graph = defaultdict(list)
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        ordered_completed_courses = []
        completed = set()

        visiting = set()

        def helper(current):
            visiting.add(current)
            for i in graph[current]:
                if i not in completed:
                    if i in visiting:
                        return False
                    flag = helper(i)
                    if not flag:
                        return False
            visiting.remove(current)
            completed.add(current)
            ordered_completed_courses.append(current)
            return True

        for i in range(numCourses):
            if i not in completed:
                if not helper(i):
                    return False

        return len(ordered_completed_courses) == numCourses


    def canFinish_temp(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_d = [0 for _ in range(numCourses)]
        graph = defaultdict(list)

        for course, prerequisite in prerequisites:
            in_d[course] += 1
            graph[prerequisite].append(course)

        zero_ins = []
        for i in range(len(in_d)):
            if in_d[i] == 0:
                zero_ins.append(i)

        processed = []
        while len(zero_ins):
            current = zero_ins.pop()
            for i in graph[current]:
                in_d[i] -= 1
                if in_d[i] == 0:
                    zero_ins.append(i)
            processed.append(i)

        return len(processed) == numCourses

    def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_d = [[] for _ in range(numCourses)]

        visited, visiting = set(), set()
        for i, j in prerequisites:
            in_d[j].append(i)

        def helper(node):
            if node in visited:
                return True
            visiting.add(node)

            for i in in_d[node]:
                if i not in visited and i not in visiting:
                    temp = helper(i)
                    if not temp:
                        return False
                # since previous condition is
                # if i not in visited and i not in visiting:
                # so this condition will only be valid if
                # a cycle is occured

                elif i in visiting:
                    return False

                elif i in visited:
                    continue

            visiting.remove(node)
            visited.add(node)

            return True
        # for loop is needed here because the first few node may not
        # have in_d so we can't reach other nodes
        for i in range(numCourses):
            current = helper(i)
            if not current:
                return False

            if len(visited) == numCourses:
                return True

        return False

    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degrees = {my_key: set()
                      for my_key in [i for i in range(numCourses)]}
        for current in prerequisites:
            course, prerequisite = current
            in_degrees[course].add(prerequisite)

        temp = sorted(list(in_degrees.items()), key=lambda x: len(x[1]))

        while True:
            if len(temp) == 0:
                return True
            if all([len(i[1]) > 0 for i in temp]):
                return False
            temp = sorted(temp, key=lambda x: len(x[1]))
            while len(temp):
                key, _values = temp[0]
                if len(in_degrees[key]) == 0:
                    for j in range(numCourses):
                        if j != key and key in in_degrees[j]:
                            in_degrees[j].remove(key)
                    temp = temp[1:]
                else:
                    break

# @lc code=end
