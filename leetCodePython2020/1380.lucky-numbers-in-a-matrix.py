#
# @lc app=leetcode id=1380 lang=python3
#
# [1380] Lucky Numbers in a Matrix
#
# @lc code=start


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:

        lucky_nums = set()

        m, n = len(matrix), len(matrix[0])

        for i in range(m):

            current_row = matrix[i]
            row_lucky = min(current_row)
            j = current_row.index(row_lucky)

            is_max = True

            for k in range(m):
                print(matrix[k][j])
                if matrix[k][j] > row_lucky:
                    is_max = False
                    break
            if is_max:
                lucky_nums.add(row_lucky)

        return list(lucky_nums)

# @lc code=end
