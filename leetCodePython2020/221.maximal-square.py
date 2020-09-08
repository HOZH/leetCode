#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if not m:
            return 0
        n = len(matrix[0])

        # check huahua 221 soulution 2, -> using 3 overlapped sub squares
        sizes = [[0 for _ in range(n)] for _ in range(m)]
        ans = 0

        for i in range(m):
            for j in range(n):
                sizes[i][j] = ord(matrix[i][j])-48

                if sizes[i][j] == 0:
                    continue

                if i == 0 or j == 0:
                    pass

                # elif i==0:
                #     sizes[i][j]=sizes[i][j-1]+1
                # elif j==0:
                #     sizes[i][j]=sizes[i-1][j]+1
                else:
                    sizes[i][j] = min(
                        sizes[i-1][j-1], sizes[i-1][j], sizes[i][j-1])+1

                ans = max(ans, sizes[i][j]**2)

        return ans

    def maximalSquare_temp(self, matrix: List[List[str]]) -> int:

        m = len(matrix)
        if not m:
            return 0
        n = len(matrix[0])

        sums = [[0 for _ in range(n+1)] for _ in range(m+1)]

        # print(m+1,n+1)
        # print(len(sums),len(sums[0]))

        for i in range(1, m+1):
            for j in range(1, n+1):
                # print(i,j)
                # it's actually matrix[i][j] since indexes are 1-indexed
                sums[i][j] = ord(matrix[i-1][j-1])-48\
                    + sums[i-1][j]\
                    + sums[i][j-1]\
                    - sums[i-1][j-1]

        ans = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                for k in range(min(m-i+1, n-j+1), -1, -1):

                    temp = sums[i+k-1][j+k-1]\
                        - sums[i+k-1][j-1]\
                        - sums[i-1][j+k-1]\
                        + sums[i-1][j-1]
                    if temp == k**2:
                        ans = max(ans, temp)
                        break

        return ans

    def maximalSquare_85_like(self, matrix: List[List[str]]) -> int:

        row_c = len(matrix)
        if row_c == 0:
            return 0
        col_c = len(matrix[0])

        dp = [[0 for _ in range(col_c)] for _ in range(row_c)]

        for i in range(row_c):
            for j in range(col_c):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = (0 if j == 0 else dp[i][j-1])+1
        ans = 0
        for i in range(row_c):
            for j in range(col_c):
                length = float('inf')
                for k in range(i, row_c):
                    # find the width that can increase the height of the area
                    length = min(length, dp[k][j])

                    if length == 0:
                        break
                    if length == (k-i+1):
                        ans = max(ans, length*(k-i+1))
        return ans

# @lc code=end
