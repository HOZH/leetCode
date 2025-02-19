#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, curr, p2 = 0, 0, len(nums) - 1  # 初始化指针

        while curr <= p2:
            if nums[curr] == 0:  # 遇到 0，交换到左侧
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:  # 遇到 2，交换到右侧
                nums[p2], nums[curr] = nums[curr], nums[p2]
                p2 -= 1  # 注意这里 curr 不能增加
            else:  # 遇到 1，跳过
                curr += 1
        
# @lc code=end

