#
# @lc app=leetcode id=1700 lang=python3
#
# [1700] Number of Students Unable to Eat Lunch
#

# @lc code=start
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = [0, 0]
        for student in students:
            counts[student] += 1

        for sandwich in sandwiches:
            if counts[sandwich] == 0:
                return counts[0] + counts[1]
            counts[sandwich] -= 1

        return 0

    def countStudents_with_nested_loop(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        while len(sandwiches):
            student_count_down = len(sandwiches)
            while student_count_down:
                current_sandwich = sandwiches[0]
                current_student = students.popleft()
                if current_student != current_sandwich:
                    students.append(current_student)
                else:
                    sandwiches.popleft()
                    break
                student_count_down -= 1
            # if we iterate through all the remaining students and still nobody wannna take
            # first sanwich, we return length of students remaining
            if student_count_down < 1:
                return len(students)
        return 0


# @lc code=end
