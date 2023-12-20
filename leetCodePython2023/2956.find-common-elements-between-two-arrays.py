#
# @lc app=leetcode id=2956 lang=python3
#
# [2956] Find Common Elements Between Two Arrays
#

# @lc code=start
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1, set2 = set(nums1), set(nums2)
        a, b = 0, 0
        for i in nums1:
            if i in set2:
                a += 1
        for i in nums2:
            if i in set1:
                b += 1

        return [a, b]

# @lc code=end
