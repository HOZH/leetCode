#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        courses = [[] for _ in range(numCourses)]

        for i, j in prerequisites:
            courses[j].append(i)

        visited = set()
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

            visited.add(current)
            visiting.remove(current)

            return True

        for i in range(numCourses):

            temp = dfs(i)

            if not temp:
                return False

            elif len(visited) == numCourses:
                return True

            visiting = set()

        return False

    def canFinish_temp1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        courses = [set() for _ in range(numCourses)]
        counts = [i for i in range(numCourses)]
        for i, j in prerequisites:
            courses[i].add(j)

        while True:
            counts.sort(key=lambda x: len(courses[x]))
            if len(counts) == 0:
                return True

            if len(courses[counts[0]]) != 0:
                return False

            current = counts[0]

            counts = counts[1:]

            for i in counts:
                courses[i] -= {current}

    def canFinish_temp(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # can use set to boost up speed, use heap maybe -> use tuple to wrap the original data with first ele in the wrapped tuple set to data's len
        courses = [[i] for i in range(numCourses)]
        for i, j in prerequisites:
            courses[i].append(j)

        while True:
            courses.sort(key=len)
            if len(courses) == 0:
                return True

            if len(courses[0]) != 1:
                return False

            current = courses[0][0]

            courses = courses[1:]

            for i in range(len(courses)):
                if current in courses[i]:
                    courses[i].remove(current)

                # @lc code=end
