#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start

from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        c1, c2 = Counter(nums1), Counter(nums2)

        # c3 = c1-c2
        # c4 = c1-c3

        result = []
        # for key, count in c4.items():
        #     result.extend([key]*count)
        for key, count in (c1&c2).items():
            result.extend([key]*count)

        return result

# @lc code=end
