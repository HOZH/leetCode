#
# @lc app=leetcode id=1042 lang=python3
#
# [1042] Flower Planting With No Adjacent
#


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:

        dic = dict(zip(range(1, N+1), list([set(), set()] for i in range(N))))

        for i, j in paths:
            dic[i][0].add(j)
            dic[j][0].add(i)

        flowers = set((1, 2, 3, 4))

        answers = list(-1 for i in range(N))

        for i in dic:

            outter_current = dic[i]

            flower_taken = flowers.difference(outter_current[1]).pop()
            answers[i-1] = flower_taken

            for j in outter_current[0]:

                dic[j][1].add(flower_taken)

        return answers
