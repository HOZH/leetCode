#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        first_items = [i[0] for i in matrix]
        l, r = 0, len(matrix)

        while l < r:
            m = l + (r - l) // 2
            if first_items[m] > target:
                r = m
            else:
                l = m + 1

        row = l-1 if l >= 1 else 0
        arr = matrix[row]
        l, r = 0, len(arr)

        while l < r:
            pivot = l + (r - l) // 2
            if arr[pivot] == target:
                return True
            elif arr[pivot] > target:
                r = pivot
            else:
                l = pivot + 1
        return False


# @lc code=end
