#
# @lc app=leetcode id=1876 lang=python3
#
# [1876] Substrings of Size Three with Distinct Characters
#

# @lc code=start
from collections import deque


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        length = len(s)
        if length < 3:
            return 0

        stack = deque([*s[:3]])
        ans = 1 if len(set(stack)) == 3 else 0

        for i in range(3, length):
            stack.popleft()
            stack.append(s[i])
            if len(set(stack)) == 3:
                ans += 1

        return ans


# @lc code=end
