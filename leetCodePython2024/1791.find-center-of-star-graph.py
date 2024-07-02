#
# @lc app=leetcode id=1791 lang=python3
#
# [1791] Find Center of Star Graph
#

# @lc code=start
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        counter = dict()
        for i, j in edges:
            if i not in counter:
                counter[i] = 1
            else:
                return i
            if j not in counter:
                counter[j] = 1
            else:
                return j


# @lc code=end
