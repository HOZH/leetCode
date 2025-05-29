#
# @lc app=leetcode id=1762 lang=python3
#
# [1762] Buildings With an Ocean View
#

# @lc code=start
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        current_max = float('-inf')
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > current_max:
                ans.append(i)
            current_max = max(current_max, heights[i])

        return ans[::-1]

# @lc code=end
