#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#


class Solution:

    def helper(self, num, current_row):


        if current_row < num+1:

            current = [1] * current_row

            if current_row > 2:

                for i in range(1, current_row - 1):
                    prev_row = self.answer[current_row - 2]
                    current[i] = prev_row[i - 1] + prev_row[i]

            self.answer.append(current)


            self.helper(num, current_row + 1)

    def generate(self, numRows):

        self.answer = list()

        self.helper(numRows, 1)

        return self.answer
