#
# @lc app=leetcode id=1089 lang=python3
#
# [1089] Duplicate Zeros
#

# @lc code=start
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        count = arr.count(0)
        for i in range(len(arr)-1, -1, -1):
            if i+count < len(arr):
                arr[i+count] = arr[i]
            if arr[i] == 0:
                count -= 1
                if i+count < len(arr):
                    arr[i+count] = 0

# @lc code=end
