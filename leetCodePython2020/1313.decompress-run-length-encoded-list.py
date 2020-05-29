#
# @lc app=leetcode id=1313 lang=python3
#
# [1313] Decompress Run-Length Encoded List
#

# @lc code=start


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:

        return [] if len(nums) == 0 else [nums[1]]*nums[0]+self.decompressRLElist(nums[2:])


# @lc code=end
