#
# @lc app=leetcode id=1396 lang=python3
#
# [1396] Design Underground System
#

# @lc code=start
from collections import defaultdict


class UndergroundSystem:

    def __init__(self):

        self.pairwise = defaultdict(list)
        self.checkIned = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:

        self.checkIned[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:

        checkInStationName, checkInTime = self.checkIned[id]

        self.pairwise[checkInStationName+'@'+stationName].append(t-checkInTime)
        del self.checkIned[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        temp = self.pairwise[startStation+'@'+endStation]
        return sum(temp)/len(temp)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# @lc code=end
