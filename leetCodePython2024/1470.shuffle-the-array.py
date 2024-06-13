#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#

# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        half_len = len(nums)//2
        ans = []
        for i in range(half_len):
            ans.append(nums[i])
            ans.append(nums[half_len+i])

        return ans


# @lc code=end
