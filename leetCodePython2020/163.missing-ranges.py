#
# @lc app=leetcode id=163 lang=python3
#
# [163] Missing Ranges
#

# @lc code=start
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans = []
        if nums:
            nums = [lower-1]+nums
            nums.append(upper+1)
        else:
            nums = [lower-1, upper+1]

        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 2:
                ans.append(str(nums[i]+1))
            elif nums[i+1]-nums[i] > 2:
                ans.append(str(nums[i]+1)+'->'+str(nums[i+1]-1))

        return ans


# @lc code=end
