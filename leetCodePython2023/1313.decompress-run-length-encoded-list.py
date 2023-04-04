#
# @lc app=leetcode id=1313 lang=python3
#
# [1313] Decompress Run-Length Encoded List
#

# @lc code=start
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)//2):
            ans.extend(([nums[2*i+1]]*nums[2*i]))
        
        return ans
        
# @lc code=end

