#
# @lc app=leetcode id=2089 lang=python3
#
# [2089] Find Target Indices After Sorting Array
#

# @lc code=start
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        nums.sort()
        ans = []
        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)
            elif len(ans) > 0:
                break
        return ans

# @lc code=end
