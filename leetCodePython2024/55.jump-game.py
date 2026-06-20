#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    # [2, 3, 1, 1, 4]
    # before iteration, lp = 4,
    # 1 lp i(4)+nums[i](4) = 8 >4, then update lp from 4 to 4
    # 2 lp i(3)+nums[i](1) = 3+1 = 4, then update lp from 4 to 3
    # 3 lp i(2)+nums[2](1) = 2+1 = lp(3), then update lp from 3 to 2
    # 4 lp i(1) + nums[1](3) = 1+3 = 4 > lp(2), then update lp from 2 to 1
    # 5 lp i(0) + nums[0][3] = 0+3 = 3 > lp(1), then update lp from 1 to 0
    def canJump(self, nums: List[int]) -> bool:
        lastPos = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0
        
# @lc code=end

