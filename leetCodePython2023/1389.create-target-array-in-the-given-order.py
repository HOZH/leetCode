#
# @lc app=leetcode id=1389 lang=python3
#
# [1389] Create Target Array in the Given Order
#

# @lc code=start
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        length = len(nums)
        target = []
        for i in range(length):
            target.insert(index[i], nums[i])

        return target

# @lc code=end
