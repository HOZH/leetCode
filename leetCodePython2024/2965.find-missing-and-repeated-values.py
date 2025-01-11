#
# @lc app=leetcode id=2965 lang=python3
#
# [2965] Find Missing and Repeated Values
#

# @lc code=start
from collections import defaultdict


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        have_not_seen = {*[i for i in range(1, (len(grid)**2)+1)]}
        counter = defaultdict(int)
        temp = [i for row in grid for i in row]
        for i in temp:
            if i in have_not_seen:
                have_not_seen.remove(i)
            counter[i] += 1

        for key, val in counter.items():
            if val == 2:
                return [key, have_not_seen.pop()]


# @lc code=end
