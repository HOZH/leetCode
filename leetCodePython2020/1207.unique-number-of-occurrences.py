#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        counter = Counter(arr)

        encoutered = set()

        for _, count in counter.items():

            if count in encoutered:
                return False

            encoutered.add(count)

        return True

# @lc code=end
