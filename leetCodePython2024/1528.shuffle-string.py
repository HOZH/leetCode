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


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = [0 for char in s]

        i = 0
        while i < len(s):
            ind_val = indices[i]
            current_char = s[i]
            output[ind_val] = current_char
            i += 1

        return ''.join(output)
