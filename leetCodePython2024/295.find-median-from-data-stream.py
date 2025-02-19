#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
class MedianFinder:

    def __init__(self):
        # Initialize self.small and self.large arrays that will be our heaps
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # Push -1 * num to self.small heap
        heapq.heappush(self.small, -1 * num)

        # Check if both heaps exist and the largest value in small heap is greater than the smallest value in large heap. This is done to make sure every num small is <= every num in large.
        if self.small and self.large and ((-1 * self.small[0]) > self.large[0]):
            # Pop from small heap, multiply that by -1 and store in val
            val = -1 * heapq.heappop(self.small)
            # Push val to large heap
            heapq.heappush(self.large, val)

        # Check if len(self.small) > (len(self.large) + 1. This is done to deal with uneven sizes as one heap can't have more than 1 value extra than the other heap.
        if len(self.small) > (len(self.large) + 1):
            # Pop from small heap, multiply that by -1 and store in val
            val = -1 * heapq.heappop(self.small)
            # Push val to large heap
            heapq.heappush(self.large, val)

        # Check if len(self.large) > (len(self.small) + 1. This is done to deal with uneven sizes as one heap can't have more than 1 value extra than the other heap.
        if len(self.large) > (len(self.small) + 1):
            # Pop from large heap, multiply that by -1 and store in val
            val = -1 * heapq.heappop(self.large)
            # Push val to small heap
            heapq.heappush(self.small, val)

    def findMedian(self) -> float:
        # Check if len(self.small) > len(self.large)
        if len(self.small) > len(self.large):
            # Return -1 * self.small[0]
            return -1 * self.small[0]
        # Else, check if len(self.small) < len(self.large)
        elif len(self.small) < len(self.large):
            # Return self.large[0]
            return self.large[0]
        # Else, return (self.large[0] + (-1 * self.small[0])) / 2
        else:
            return (self.large[0] + (-1 * self.small[0])) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

