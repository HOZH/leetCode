#
# @lc app=leetcode id=296 lang=python3
#
# [296] Best Meeting Point
#

# @lc code=start
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # self.house_list = []
        # ans = float('inf')
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 1:
        #            self.house_list.append((i,j))
        

        # def get_distance_sum(x, y):
        #     totoal_dis = 0
        #     for i, j in self.house_list:
        #         totoal_dis += abs(x-i) + abs(y-j)
        #     return totoal_dis

        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         ans = min(ans,get_distance_sum(i,j))

        # return ans
        rows = []
        cols = []

        # Collect all rows and columns where grid[row][col] == 1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    rows.append(row)
                    cols.append(col)

        # Median of rows
        row = rows[len(rows) // 2]

        # Sort columns and find the median
        cols.sort()
        col = cols[len(cols) // 2]

        def min_distance_1d(points, origin):
            return sum(abs(point - origin) for point in points)

        # Calculate the total distance
        return min_distance_1d(rows, row) + min_distance_1d(cols, col)


                    
        



        
# @lc code=end

