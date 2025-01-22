#
# @lc app=leetcode id=760 lang=python3
#
# [760] Find Anagram Mappings
#

# @lc code=start
from collections import defaultdict


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        bag = defaultdict(list)
        for i in range(len(nums2)):
            bag[nums2[i]].append(i)
        ans = []
        for i in nums1:
            ans.append(bag[i].pop())
        return ans

# @lc code=end
