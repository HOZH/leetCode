#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        sorted_lis = sorted(nums)

        return list(map(lambda x: sorted_lis.index(x), nums))
# @lc code=end
