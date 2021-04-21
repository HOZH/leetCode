#
# @lc app=leetcode id=1636 lang=python3
#
# [1636] Sort Array by Increasing Frequency
#

# @lc code=start
from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        counter = Counter(nums)

        ans = []
        for i, j in sorted(list(counter.items()), key=lambda x: (x[1], -x[0])):

            ans += j*[i]

        return ans


# @lc code=end
