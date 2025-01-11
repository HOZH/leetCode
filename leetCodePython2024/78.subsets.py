#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(2**len(nums)):
            current = []
            for j in range(len(nums)):
                if i & (1 << j):
                    current.append(nums[j])
            ans.append(current)

        return ans

# @lc code=end
