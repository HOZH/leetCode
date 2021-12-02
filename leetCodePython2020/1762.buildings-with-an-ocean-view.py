#
# @lc app=leetcode id=1762 lang=python3
#
# [1762] Buildings With an Ocean View
#

# @lc code=start
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        temp = heights[::-1]
        current_height = 0
        ans = []

        for i in range(len(temp)):
            if temp[i] > current_height:
                ans.append(i)
                current_height = temp[i]

        return list(map(lambda x: len(temp)-1-x, ans))[::-1]


# @lc code=end
