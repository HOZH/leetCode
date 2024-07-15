#
# @lc app=leetcode id=2956 lang=python3
#
# [2956] Find Common Elements Between Two Arrays
#

# @lc code=start
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1, set2 = set(nums1), set(nums2)
        ans1, ans2 = 0, 0
        for i in range(len(nums1)):
            if nums1[i] in set2:
                ans1 += 1
        for i in range(len(nums2)):
            if nums2[i] in set1:
                ans2 += 1

        return [ans1, ans2]


# @lc code=end
