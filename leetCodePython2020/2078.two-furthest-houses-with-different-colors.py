#
# @lc app=leetcode id=2078 lang=python3
#
# [2078] Two Furthest Houses With Different Colors
#

# @lc code=start
class Solution:
    def maxDistance(self, colors: List[int]) -> int:

        step = 0

        head, tail = 0, len(colors)-1
        while head < tail:
            if colors[head] != colors[tail]:
                step = max(step, abs(head-tail))
            tail -= 1

        head, tail = 0, len(colors)-1
        while head < tail:
            if colors[head] != colors[tail]:
                step = max(step, abs(head-tail))
            head += 1

        return step

# @lc code=end
