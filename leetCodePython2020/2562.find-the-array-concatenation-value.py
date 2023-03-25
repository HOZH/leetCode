#
# @lc app=leetcode id=2562 lang=python3
#
# [2562] Find the Array Concatenation Value
#

# @lc code=start
from collections import deque
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans =0
        nums = deque(nums)

        while len(nums) >1:
            ans+=int(str(nums.popleft())+str(nums.pop()))
        
        if len(nums):
            ans+=nums[0]
        
        return ans

        
# @lc code=end

