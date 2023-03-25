#
# @lc app=leetcode id=2405 lang=python3
#
# [2405] Optimal Partition of String
#

# @lc code=start

class Solution:
    def partitionString(self, s: str) -> int:

        encountered = set()
        ans = 0
        for i in s:
            if i in encountered:
                encountered = set()
                ans += 1
            encountered.add(i)

        return ans + (0 if len(encountered) == 0 else 1)

# @lc code=end
