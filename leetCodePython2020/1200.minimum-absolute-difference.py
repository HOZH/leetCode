#
# @lc app=leetcode id=1200 lang=python3
#
# [1200] Minimum Absolute Difference
#

# @lc code=start
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr.sort()
        min_diff = float('inf')
        ans = []
        for i in range(len(arr)-1):

            if arr[i+1]-arr[i] < min_diff:
                min_diff = arr[i+1]-arr[i]

        for i in range(len(arr)-1):

            if arr[i+1]-arr[i] == min_diff:
                ans.append([arr[i], arr[i+1]])

        return ans


# @lc code=end
