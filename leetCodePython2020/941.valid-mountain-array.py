#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#

# @lc code=start
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        inc, dec = False, False

        current = arr[0]

        current_index = 0

        for i in range(1, len(arr)):

            if arr[i] > current:
                inc = True
                current_index = i
                current = arr[i]
            else:
                break

        temp = -1
        for i in range(current_index+1, len(arr)):

            if arr[i] < current:
                dec = True
                temp = i
                current = arr[i]
            else:
                break

        return temp == len(arr)-1 and dec and inc


# @lc code=end
