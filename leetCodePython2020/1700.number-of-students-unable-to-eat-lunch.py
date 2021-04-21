#
# @lc app=leetcode id=1700 lang=python3
#
# [1700] Number of Students Unable to Eat Lunch
#

# @lc code=start
from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        count = len(students)
        students = deque(students)

        for i in range(len(sandwiches)):

            current_sandwich = sandwiches[i]

            students_count = len(students)

            while len(students):

                current_student = students.popleft()

                if current_student == current_sandwich:
                    count -= 1
                    break
                else:
                    students_count -= 1
                    students.append(current_student)

                if students_count == 0:
                    return count

        return count

# @lc code=end
