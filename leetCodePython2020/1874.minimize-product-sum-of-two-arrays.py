#
# @lc app=leetcode id=1874 lang=python3
#
# [1874] Minimize Product Sum of Two Arrays
#

# @lc code=start
class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:

        nums1.sort()
        nums2.sort(reverse=True)

        ans = 0

        for i in range(len(nums1)):
            ans += nums1[i]*nums2[i]

        return ans

# @lc code=end
