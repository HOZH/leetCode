#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start

from collections import OrderedDict, defaultdict


class Solution:

    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        if len(trust) == 0:
            return 1 if N == 1 else -1

        in_d, out_d = N-1, 0

        out_g = defaultdict(list)
        in_g = defaultdict(list)

        for i, j in trust:

            in_g[j].append(i)

            out_g[i].append(j)

        temp = list(filter(lambda x: len(in_g[x]) == in_d and len(out_g[x]) == out_d, [
                    i for i in range(1, N+1)]))

        return -1 if len(temp) != 1 else temp[0]

    def findJudge_temp(self, N: int, trust: List[List[int]]) -> int:

        if len(trust) == 0:
            return 1 if N == 1 else -1

        in_d, out_d = N-1, 0

        out_g = dict()
        in_g = defaultdict(list)

        for i in range(1, N+1):
            out_g[i] = []

        for i, j in trust:

            in_g[j].append(i)

            out_g[i].append(j)

        in_g = OrderedDict(
            sorted(in_g.items(), key=lambda x: len(x[1]), reverse=True))

        out_g = OrderedDict(
            sorted(out_g.items(), key=lambda x: len(x[1]), reverse=False))

        in_first_item = next(iter(in_g.items()))
        out_first_item = next(iter(out_g.items()))

        if len(in_first_item[1]) == in_d and len(out_first_item[1]) == out_d:

            if in_first_item[0] == out_first_item[0]:

                return in_first_item[0]

        return -1

# @lc code=end
