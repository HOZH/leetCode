#
# @lc app=leetcode id=813 lang=python3
#
# [813] Largest Sum of Averages
#
import statistics
# @lc code=start


class Solution:

    def largestSumOfAverages(self, A, K: int) -> float:
        # no sure why the heck statistics.mean runs so slow
        def avg(array):
            return sum(array) / len(array)
        # dp [i->sub list of A til ith ele][p->how many parts]
        dp = [[0 for _ in range(K + 1)] for _ in range(len(A))]
        means = [[0 for _ in range(len(A))] for _ in range(len(A))]

        for i in range(len(A)):
            for j in range(i, len(A)):
                # include i include j
                # means[i][j] = statistics.mean(A[i:j + 1])
                means[i][j] = avg(A[i:j + 1])

        for i in range(len(A)):
            dp[i][1] = means[0][i]

        for i in range(1, len(A)):
            for j in range(2, min(K + 1, i + 1 + 1)):
                # k+1 last_stop_index+1 -> if stop at index 2 we can divide up to 2+1 = 3 groups,  j-1 prev_groups
                for k in range(max(i - 1, j - 1 - 1), -1, -1):
                    # k exclude, i included
                    temp_last_group = means[k + 1][i]
                    temp_sum_prev = dp[k][j - 1]
                    dp[i][j] = max(
                        dp[i][j], temp_last_group + temp_sum_prev)

        return dp[-1][-1]

    # def largestSumOfAverages(self, A, K: int) -> float:

    #     if K == 0:
    #         return mean(A)

    #     lis_len = len(A)
    #     if K >= lis_len:
    #         return sum(A)
    #     means = [[0 for _ in range(lis_len)] for _ in range(lis_len)]
    #     # print(means)

    #     for i in range(lis_len):
    #         for j in range(i, lis_len):
    #             # print(i,j,mean(A[i:j+1]))
    #             means[i][j] = mean(A[i:j+1])

    #     dp = [[0 for _ in range(lis_len + 1)] for _ in range(K + 1)]

    #     for i in range(1, lis_len + 1):
    #         # dp[1][i] = mean(A[:i])
    #         dp[1][i] = means[0][i-1]

    #     for i in range(2, K + 1):
    #         for j in range(i, lis_len + 1):
    #             # temp_lis = []
    #             local_max = 0
    #             for p in range(1, j):
    #                 # temp = dp[i - 1][p] + mean(A[p:j])
    #                 temp = dp[i-1][p]+means[p][j-1]
    #                 # print(A[p:j],mean(A[p:j]),means[p][j-1],p,j-1)

    #                 import sys
    #                 # sys.exit(0)
    #                 # temp = dp[i - 1][p] + means[p-1][j]

    #                 if temp > dp[i][j]:
    #                     dp[i][j] = temp
    #                 # temp_lis.append(temp)
    #             # dp[i][j] = max(temp_lis)

    #     return dp[K][lis_len]

# @lc code=end
