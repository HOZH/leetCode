#
# @lc app=leetcode id=2496 lang=python3
#
# [2496] Maximum Value of a String in an Array
#

# @lc code=start
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = 0
        for i in strs:
            if i.isdigit():
                ans = max(ans, int(i))
            else:
                ans = max(ans, len(i))
        return ans

# @lc code=end
