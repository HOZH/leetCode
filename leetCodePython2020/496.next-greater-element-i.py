#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        indexs = []
        ans = []

        for i in nums1:
            indexs.append(nums2.index(i))

        for i in indexs:
            current = nums2[i]
            found = False
            for j in range(i+1, len(nums2)):
                if nums2[j] > current:
                    ans.append(nums2[j])
                    found = True
                    break
            if not found:
                ans += [-1]

        return ans


# @lc code=end
