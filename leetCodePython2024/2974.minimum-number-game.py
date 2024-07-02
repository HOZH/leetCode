#
# @lc app=leetcode id=2974 lang=python3
#
# [2974] Minimum Number Game
#

# @lc code=start
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums = sorted(nums,reverse=True)
        ans = []
        while len(nums) > 0:
            a = nums.pop()
            b = nums.pop()
            ans.extend([b, a])

        return ans


# @lc code=end
