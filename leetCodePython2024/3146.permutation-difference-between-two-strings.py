#
# @lc app=leetcode id=3146 lang=python3
#
# [3146] Permutation Difference between Two Strings
#

# @lc code=start
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        bag = dict()
        for i in range(len(s)):
            bag[s[i]] = i
        ans = 0
        for i in range(len(s)):
            ans += abs(i-bag[t[i]])

        return ans


# @lc code=end
