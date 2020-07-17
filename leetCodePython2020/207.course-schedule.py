#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # can use set to boost up speed
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
