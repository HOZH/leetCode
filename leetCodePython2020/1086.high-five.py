#
# @lc app=leetcode id=1086 lang=python3
#
# [1086] High Five
#

# @lc code=start
from heapq import heapify, heappush, heappop
from collections import defaultdict


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        students = defaultdict(list)

        for id, score in items:

            heappush(students[id], -score)

        ans = []

        for student in students.keys():

            temp = 0

            for _ in range(5):
                temp += heappop(students[student])

            avg = (-temp)//5

            ans.append([student, avg])

        return sorted(ans, key=lambda x: x[0])


# @lc code=end
