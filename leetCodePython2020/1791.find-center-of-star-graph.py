#
# @lc app=leetcode id=1791 lang=python3
#
# [1791] Find Center of Star Graph
#

# @lc code=start
from collections import Counter


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # could use set to boost up performance
        return Counter([j for i in edges for j in i]).most_common()[0][0]


# @lc code=end
