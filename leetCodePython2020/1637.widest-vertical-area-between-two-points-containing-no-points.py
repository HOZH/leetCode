#
# @lc app=leetcode id=1637 lang=python3
#
# [1637] Widest Vertical Area Between Two Points Containing No Points
#

# @lc code=start
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        temp = [i[0] for i in points]
        temp.sort()

        ans = 0

        for i in range(1, len(temp)):

            ans = max(ans, temp[i]-temp[i-1])

        return ans

# @lc code=end
