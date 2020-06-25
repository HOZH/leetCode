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

        l, r = 0, len(matrix)-1
        row = -1
        while l <= r:
            pivot = l+(r-l)//2
            if first_items[pivot] == target:
                return True

            elif target < first_items[pivot]:
                r = pivot-1

            else:
                l = pivot+1

        row = row if row != -1 else r

        arr = matrix[row]

        l, r = 0, len(arr)-1
        while l <= r:
            pivot = l+(r-l)//2
            if arr[pivot] == target:
                return True

            elif target < arr[pivot]:
                r = pivot-1

            else:
                l = pivot+1

        return False


# @lc code=end
