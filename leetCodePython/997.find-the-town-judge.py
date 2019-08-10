#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

from collections import Counter


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:


        if N ==1:

            return 1

        dic = dict()

        for i, j in trust:

            if j not in dic:

                dic[j] = set()

            dic[j].add(i)


        found = False


        min_count = N-1

        for i in dic:

            if len(dic[i]) >= min_count:

                found = True

                for j in dic:

                    if j != i:

                        if i in dic[j]:

                            found = False
                            

                return i if found else -1

        return -1
