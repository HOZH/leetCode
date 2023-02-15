#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        row_len = len(matrix)
        if not row_len:
            return 0
        col_len = len(matrix[0])

        # dp[i][j] -> max seq length of consecutive 1s end in index i,j
        dp = [list(map(lambda x:int(x), matrix[i])) for i in range(row_len)]

        for i in range(row_len):
            for j in range(col_len):
                if dp[i][j] != 0:
                    if j != 0:
                        dp[i][j] = dp[i][j-1]+1

        ans = 0

        for i in range(row_len):
            for j in range(col_len):

                if dp[i][j] != 0:
                    if i > 0 and dp[i-1][j] >= dp[i][j]:
                        continue

                    min_length = float('inf')

                    for k in range(i, row_len):
                        if dp[k][j] == 0:
                            break
                        else:
                            min_length = min(min_length, dp[k][j])

                            if min_length*(row_len-1-i+1) < ans:
                                break

                            ans = max(ans, min_length*(k-i+1))

        return ans


# @lc code=end
