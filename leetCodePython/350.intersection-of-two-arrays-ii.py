#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

       
        return (collections.Counter(nums1) & collections.Counter(nums2)).elements()
