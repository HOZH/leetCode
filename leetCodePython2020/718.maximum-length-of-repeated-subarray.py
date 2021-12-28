#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#

# @lc code=start
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:

        n = len(A)
        m = len(B)

        # Edge cases.
        if m == 0 or n == 0:
            return 0

        if n == 1 and m == 1:
            if A[0] == B[0]:
                return 1
            else:
                return 0

        # Initializing first row and column with 0 (for ease i intialized everthing 0 :p)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        # this code is a lot like longest common subsequence(only else condition is different).
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                # else:
                #     dp[i][j] = 0

        return max([item for sublist in dp for item in sublist])


# @lc code=end
