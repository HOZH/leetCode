#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
import heapq
from collections import defaultdict


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:

        temp_heap = self.dic[key]

        heapq.heappush(temp_heap, (-timestamp, value))

        self.dic[key] = temp_heap

    def get(self, key: str, timestamp: int) -> str:

        temp_heap = self.dic[key]
        place_holder = []

        while len(temp_heap) > 0:
            temp = heapq.heappop(temp_heap)
            place_holder.append(temp)

            if -temp[0] <= timestamp:
                break

        for i in place_holder:
            heapq.heappush(temp_heap, i)

        # temp_values = temp_heap+place_holder
        # heapq.heapify(temp_values)
        # self.dic[key] = temp_values

        return temp[1] if -temp[0] <= timestamp else ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
