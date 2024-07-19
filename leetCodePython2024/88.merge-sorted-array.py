#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for _ in range(len(nums1) - m):
            nums1.pop()
        for _ in range(len(nums2) - n):
            nums2.pop()

        m, n = len(nums1), len(nums2)
        if n == 0:
            return
        elif m == 0:
            nums1.extend(nums2)
            return

        pt1, pt2 = 0, 0
        nums1_used = 0
        while pt1 < m + n and pt2 < n and nums1_used < m:
            if nums1[pt1] < nums2[pt2]:
                nums1_used += 1
                pt1 += 1
            else:
                nums1.insert(pt1, nums2[pt2])
                pt1 += 1
                pt2 += 1
        nums1.extend(nums2[pt2:])


# @lc code=end
