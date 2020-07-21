#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start

from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        d = defaultdict(list)

        for s, e in tickets:

            d[s].append(e)

        for i in d.keys():

            d[i].sort()

        route = []

        def helper(start):

            while len(d[start]) > 0:

                temp = d[start
                d[start] = d[start][1:]

                helper(temp)

            route.append(start)

        helper('JFK')

        return route[::-1]


# @lc code=end
