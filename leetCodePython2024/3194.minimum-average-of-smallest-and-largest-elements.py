#
# @lc app=leetcode id=3194 lang=python3
#
# [3194] Minimum Average of Smallest and Largest Elements
#

# @lc code=start
from collections import deque


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        count = len(nums)//2
        avg = []
        nums.sort()
        nums = deque(nums)
        while count != 0:
            local_min = nums.popleft()
            local_max = nums.pop()
            avg.append((local_min+local_max)/2)
            count -= 1

        return min(avg)

# @lc code=end
