#
# @lc app=leetcode id=1198 lang=python3
#
# [1198] Find Smallest Common Element in All Rows
#

# @lc code=start
from functools import reduce
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        sets=[]
        for row in mat:
            sets.append(set(row))
        temp = list(reduce(lambda x,y:x&y,sets))
        if not len(temp):
            return -1
        return min(temp)
        
        
# @lc code=end

