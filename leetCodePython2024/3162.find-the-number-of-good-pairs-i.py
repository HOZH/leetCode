#
# @lc app=leetcode id=3162 lang=python3
#
# [3162] Find the Number of Good Pairs I
#

# @lc code=start
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                ans+= nums1[i] % (nums2[j]*k) == 0

        return ans
        
# @lc code=end

