#
# @lc app=leetcode id=2363 lang=python3
#
# [2363] Merge Similar Items
#

# @lc code=start
from collections import defaultdict

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:

        bag = defaultdict(int)
        for value, weight in [*items1, *items2]:
            bag[value]+=weight

        return sorted(list(bag.items()))

        
# @lc code=end

