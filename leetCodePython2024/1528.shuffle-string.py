#
# @lc app=leetcode id=1528 lang=python3
#
# [1528] Shuffle String
#

# @lc code=start
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [0]*len(s)
        for i in range(len(s)):
            ans[indices[i]] = s[i]

        return ''.join(ans)
# @lc code=end
