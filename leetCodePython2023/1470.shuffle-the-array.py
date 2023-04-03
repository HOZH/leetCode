#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#

# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(len(nums)//2):
            ans.extend([nums[i], nums[n+i]])

        return ans

# @lc code=end
