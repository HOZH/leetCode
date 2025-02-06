#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
# from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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

    def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
