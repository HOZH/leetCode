#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
from collections import deque, defaultdict


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        map = defaultdict(lambda: -1)
        stack = deque()
        length = len(nums)
        count_to_find = len(nums)-nums.count(max(nums))

        for _ in range(2):
            for n in range(length):
                while stack and stack[0][1] < nums[n]:
                    temp = stack.popleft()
                    if temp[0] not in map:
                        map[temp[0]] = nums[n]
                        if len(map) == count_to_find:
                            return [map[x] for x in range(length)]
                stack.appendleft((n, nums[n]))

            if len(map) == count_to_find:
                break

        return [map[x] for x in range(length)]

# @lc code=end
