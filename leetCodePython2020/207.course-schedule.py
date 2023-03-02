#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # hold_others = [[] for _ in range(numCourses)]
        # in_d = [0] * numCourses
        # for i, j in prerequisites:
        #     if i == j:
        #         return False
        #     hold_others[i].append(j)
        #     in_d[j] += 1
        # finished = set()
        # remaining = set([i for i in range(numCourses)])
        # while len(remaining):
        #     can_proceed = False
        #     pending_remove = set()
        #     for current in remaining:
        #         if in_d[current] == 0:
        #             can_proceed = True
        #             finished.add(current)
        #             pending_remove.add(current)
        #             for j in hold_others[current]:
        #                 in_d[j]-=1
        #     if not can_proceed:
        #         return False
        #     remaining -=pending_remove
        # return True

        # return

        # find cycle -> visiting means the current node had been met in previous steps

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

    def canFinish_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

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
