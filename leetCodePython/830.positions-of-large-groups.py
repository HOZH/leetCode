#
# @lc app=leetcode id=830 lang=python3
#
# [830] Positions of Large Groups
#


class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:

        length = len(S)
        if length == 0:
            return []

        prev = S[0]
        head, tail = 0, 0
        answers = list()
        for i in range(1, length):

            current = S[i]

            if current == prev:

                tail += 1

            else:

                answers.append([head, tail])
                head = i
                tail = i

            prev = current
        answers.append([head, tail])

        return list(filter(lambda x: x[1]-x[0] > 1, answers))
