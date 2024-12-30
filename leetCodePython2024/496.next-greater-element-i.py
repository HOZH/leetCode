#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            next_greater = -1
            found_current = False
            for j in nums2:
                if j == i:
                    found_current = True
                if found_current and j > i:
                    next_greater = j
                    break
            ans.append(next_greater)

        return ans

# @lc code=end
