#
# @lc app=leetcode id=1133 lang=python3
#
# [1133] Largest Unique Number
#

# @lc code=start
from collections import Counter


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        counter = Counter(nums)
        temp = []

        for ele, freq in counter.items():
            if freq == 1:
                temp.append(ele)

        return sorted(temp)[-1] if len(temp) else -1


# @lc code=end
