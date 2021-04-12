#
# @lc app=leetcode id=1502 lang=python3
#
# [1502] Can Make Arithmetic Progression From Sequence
#

# @lc code=start
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        if len(arr) < 2:
            return True
        arr.sort()

        diff = arr[1]-arr[0]

        for i in range(2, len(arr)):

            if arr[i]-arr[i-1] != diff:
                return False

        return True

# @lc code=end
