#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str):
        len1, len2 = len(word1), len(word2)

        if len(word1) == 0:
            return len2
        if len2 == 0:
            return len1

        # dp[i][j] implies the minimun cost for converting first i chars of word1 to first j chars of word2

        # pad by 1 index for both h,v
        # dp min cost of case where i-th of word1 matches j-th of word2
        # by assign their value recursively, we can ensure digits prior to i-th and j-th
        # are matched as well?
        # no sure ->  2nd of word1 matches 5th of word2
        # assume 1st,2nd digit of both have the same value
        # dp[2][5]would be 3 if only insertion is taking care of
        # just the thought, gotta check back later
        dp = [[0]*(len2+1) for _ in range(len1+1)]

        for i in range(len1+1):
            dp[i][0] = i

        for i in range(len2+1):
            dp[0][i] = i

        for i in range(1, len1+1):
            for j in range(1, len2+1):
                # dp[i-1][j]+1 implies (i-1)th of word1 already matched jth of word2
                # therefore it will perform a deletion of last digit of word1 at cost 1
                # word1[i-1] and word2[j-1] since they're in 1-indexed table

                dp[i][j] = min(dp[i-1][j-1]+(0 if word1[i-1] == word2[j-1] else 1),
                               dp[i-1][j]+1,
                               dp[i][j-1]+1)

                # dp[-1][-1] where the min cost that all j matches all i
        return dp[-1][-1]

# @lc code=end
