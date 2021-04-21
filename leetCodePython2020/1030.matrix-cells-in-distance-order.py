#
# @lc app=leetcode id=1030 lang=python3
#
# [1030] Matrix Cells in Distance Order
#

# @lc code=start
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:

        coords = []

        for i in range(R):
            for j in range(C):

                coords.append([i, j])

        coords.sort(key=lambda x: abs(x[0]-r0)+abs(x[1]-c0))

        return coords


# @lc code=end
