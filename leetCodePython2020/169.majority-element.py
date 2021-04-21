#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start

from collections import defaultdict
import math


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        dic = defaultdict(int)

        for i in nums:
            dic[i] += 1

        limit = math.ceil(len(nums)/2)

        for i in dic.keys():
            if dic[i] >= limit:
                return i


# @lc code=end
