#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#

# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_nums = []
        prev = 0
        for i in arr:
            missing_nums.extend(range(prev + 1, i))
            prev = i
        for i in range(arr[-1]+1, 2002):
            missing_nums.append(i)
        return missing_nums[k-1]


# @lc code=end
