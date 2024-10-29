#
# @lc app=leetcode id=3131 lang=python3
#
# [3131] Find the Integer Added to Array I
#

# @lc code=start
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        return nums2[0]-nums1[0]

# @lc code=end
