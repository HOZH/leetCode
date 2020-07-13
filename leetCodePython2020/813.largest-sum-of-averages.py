#
# @lc app=leetcode id=813 lang=python3
#
# [813] Largest Sum of Averages
#
import statistics
# @lc code=start


class Solution:
    def largestSumOfAverages(self, A, K: int) -> float:

        if K == 0:
            return mean(A)

        lis_len = len(A)
        if K >= lis_len:
            return sum(A)
        means = [[0 for _ in range(lis_len)] for _ in range(lis_len)]
        # print(means)

        for i in range(lis_len):
            for j in range(i, lis_len):
                # print(i,j,mean(A[i:j+1]))
                means[i][j] = mean(A[i:j+1])

        dp = [[0 for _ in range(lis_len + 1)] for _ in range(K + 1)]

        for i in range(1, lis_len + 1):
            # dp[1][i] = mean(A[:i])
            dp[1][i] = means[0][i-1]

        for i in range(2, K + 1):
            for j in range(i, lis_len + 1):
                # temp_lis = []
                local_max = 0
                for p in range(1, j):
                    # temp = dp[i - 1][p] + mean(A[p:j])
                    temp = dp[i-1][p]+means[p][j-1]
                    # print(A[p:j],mean(A[p:j]),means[p][j-1],p,j-1)

                    import sys
                    # sys.exit(0)
                    # temp = dp[i - 1][p] + means[p-1][j]

                    if temp > dp[i][j]:
                        dp[i][j] = temp
                    # temp_lis.append(temp)
                # dp[i][j] = max(temp_lis)

        return dp[K][lis_len]

# @lc code=end
