#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start

from bisect import bisect
# import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        # k is always valid

        # return sorted([i for j in matrix for i in j])[k-1]

        l, r = matrix[0][0], matrix[-1][-1]

        while l < r:
            pivot = l + (r-l)//2
            if sum(bisect(row, pivot) for row in matrix) < k:
                l = pivot+1
            else:
                r = pivot

        return l

        # heapq.heapify(matrix)

        # temp = None
        # for _ in range(k):
        #     temp = heapq.heappop(matrix)
        #     if len(temp) > 1:
        #         heapq.heappush(matrix, temp[1:])

        # return temp[0]


# @lc code=end
