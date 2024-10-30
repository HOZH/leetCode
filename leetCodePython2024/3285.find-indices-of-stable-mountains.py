#
# @lc app=leetcode id=3285 lang=python3
#
# [3285] Find Indices of Stable Mountains
#

# @lc code=start
class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        ans = []
        for i in range(1, len(height)):
            if height[i-1] > threshold:
                ans += [i]

        return ans

# @lc code=end
