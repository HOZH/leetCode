#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        courses = [[] for _ in range(numCourses)]

        for i, j in prerequisites:
            courses[j].append(i)

        visited = list()
        visiting = set()

        def dfs(current):
            visiting.add(current)
            for i in courses[current]:

                if i not in visited and i not in visiting:

                    local_temp = dfs(i)
                    if not local_temp:
                        return False
                elif i in visiting:
                    return False
            visited.append(current)

            visiting.remove(current)

            return True

        for i in range(numCourses):

            if i not in visited:

                temp = dfs(i)

                if not temp:
                    return []

                elif len(visited) == numCourses:
                    return visited[::-1]

                visiting = set()

        return []

    def findOrder_temp(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # can use set to boost up speed, use heap maybe -> use tuple to wrap the original data with first ele in the wrapped tuple set to data's len
        courses = [[i] for i in range(numCourses)]
        result = []
        for i, j in prerequisites:
            courses[i].append(j)

        while True:
            courses.sort(key=len)
            if len(courses) == 0:
                return result

            if len(courses[0]) != 1:
                return []

            current = courses[0][0]
            result.append(current)

            courses = courses[1:]

            for i in range(len(courses)):
                if current in courses[i]:
                    courses[i].remove(current)

# @lc code=end
