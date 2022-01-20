#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        if not len_s:
            return True
        ps, pt = 0, 0

        while ps < len_s and pt < len(t):
            if s[ps] == t[pt]:
                ps += 1
            pt += 1
            if ps == len_s:
                return True
        return False


# @lc code=end
