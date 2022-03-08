#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
from collections import deque


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        if len(set(nums[:k+1])) < len(nums[:k+1]):
            return True
        prev_lis = deque(nums[0:k])
        prev_set = set(prev_lis)
        for i in range(k, len(nums)):
            current = nums[i]
            if current in prev_set:
                return True

            prev_set.remove(prev_lis.popleft())
            prev_lis.append(current)
            prev_set.add(current)

        return False

# @lc code=end
