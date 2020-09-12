#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start

from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # use greedy

        d = defaultdict(list)

        for s, e in tickets:

            d[s].append(e)
        # sort by lex order
        for i in d.keys():
            d[i].sort()

        route = []

        # [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
        # jfk1 -> kul(append) ->go back to jfk1
        # -> nrt -> jfk2(append) -> go back to nrt(append)
        # go back to jfk1(append)
        # kul jfk2 nrt jfk1
        # then reverse the route

        def helper(start):

            while len(d[start]):
                temp = d[start][0]
                d[start] = d[start][1:]
                helper(temp)
            route.append(start)

        helper('JFK')

        return route[::-1]

# @lc code=end
