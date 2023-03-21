#
# @lc app=leetcode id=2357 lang=python3
#
# [2357] Make Array Zero by Subtracting Equal Amounts
#

# @lc code=start
from collections import deque
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums)-{0})

        # nums.sort()
        # nums = deque(nums)
        # ans = 0
        # while nums.count(0) != len(nums):
        #     while nums[0]==0:
        #         nums.popleft()
        #     nums = deque(map(lambda x:x-nums[0],nums))
        #     ans+=1

        # return ans


# @lc code=end
