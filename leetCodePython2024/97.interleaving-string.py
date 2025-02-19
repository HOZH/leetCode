#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # If the length of s3 is not equal to the sum of lengths of s1 and s2, return False
        if len(s1) + len(s2) != len(s3):
            return False

        # Initialize the DP table with False
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        # Base case: empty strings of s1 and s2 form the empty string s3
        dp[0][0] = True

        # Fill the DP table
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i > 0 and dp[i-1][j] and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = True
                if j > 0 and dp[i][j-1] and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = True

        # The answer will be at dp[len(s1)][len(s2)]
        return dp[len(s1)][len(s2)]

# @lc code=end

