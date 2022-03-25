#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#

# @lc code=start
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        ans = []
        while i < len(firstList) and j < len(secondList):
            left1, right1 = firstList[i]
            left2, right2 = secondList[j]
            left = max(left1, left2)
            right = min(right1, right2)
            if left <= right:
                ans.append([left, right])
            if right1 <= right2:
                i += 1
            else:
                j += 1
        return ans

        
# @lc code=end

