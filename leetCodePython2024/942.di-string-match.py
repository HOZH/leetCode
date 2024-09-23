#
# @lc app=leetcode id=942 lang=python3
#
# [942] DI String Match
#

# @lc code=start
from collections import deque


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        nums = deque([i for i in range(len(s)+1)])
        ans = []
        for i in s:
            if i == 'I':
                ans.append(nums.popleft())
            else:
                ans.append(nums.pop())
        ans.append(nums.pop())
        return ans

# @lc code=end
