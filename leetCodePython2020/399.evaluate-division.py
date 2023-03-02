#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start

from collections import defaultdict
from functools import lru_cache

# can optimize spped by choose data structure more wisely


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # (a/b)*(b/c)  => a/c
        # find a path between a and c => a-b-c
        # a / a self circuit

        # a/b = 0.5 => b/a = 2

        # get vals

        vals = set()
        for i in equations:
            for j in i:
                vals.add(j)

        vals = list(vals)

        # print(vals)
        graph = defaultdict(list)

        # construct a graph

        for i, j in equations:
            graph[i].append(j)
            graph[j].append(i)

        # print(graph)
        # print(max(graph))
        lru_cache(None)

        def helper(v, vis, path, end):

            vis[v] = True

            for i in graph[v]:
                if i == end:
                    return path+[i]
                if vis[i] == False:
                    temp = helper(i, vis, path+[i], end)
                    if len(temp) > 0:
                        return temp

            return []

        def find_result(start, end):

            if start == end and start in vals:
                return 1.0

            visited = defaultdict(lambda: False)

            temp = helper(start, visited, [start], end)

            if len(temp) == 0:
                return -1.0

            else:
                result = 1
                # invert = False
                # if[temp[0], temp[1]] in equations:
                #     index = equations.index([temp[0], temp[1]])
                # else:
                #     index = equations.index([temp[1], temp[0]])
                #     invert = True

                # result = values[index]
                # if invert:
                #     result = 1/result

                for i in range(len(temp)-1):
                    invert = False
                    if [temp[i], temp[i+1]] in equations:
                        index = equations.index([temp[i], temp[i+1]])
                    else:
                        index = equations.index([temp[i+1], temp[i]])
                        invert = True

                    mid = values[index]
                    if invert:
                        mid = 1/mid
                    result *= mid

                return result
        ans = []
        for i, j in queries:
            ans.append(find_result(i, j))

        return ans

        # do a dfs search to see if the graph is connected
        # remember the path

# @lc code=end
