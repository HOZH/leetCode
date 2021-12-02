#
# @lc app=leetcode id=2032 lang=python3
#
# [2032] Two Out of Three
#

# @lc code=start
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:

        set1, set2, set3 = set(nums1), set(nums2), set(nums3)

        placeholder = []
        placeholder.extend(set1)
        placeholder.extend(set2)
        placeholder.extend(set3)

        return list(set(list(filter(lambda x: placeholder.count(x) > 1, placeholder))))


# @lc code=end
