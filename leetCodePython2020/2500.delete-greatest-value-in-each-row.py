#
# @lc app=leetcode id=2500 lang=python3
#
# [2500] Delete Greatest Value in Each Row
#

# @lc code=start
from collections import defaultdict
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        if not len(grid):
            return 0
        for i in grid:
            i.sort()
        bag = defaultdict(int)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                bag[j]=max(bag[j],grid[i][j])
        
        ans = sum(bag.values())
        return ans
            
            
        
# @lc code=end

