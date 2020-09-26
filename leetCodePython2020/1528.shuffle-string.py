#
# @lc app=leetcode id=1528 lang=python3
#
# [1528] Shuffle String
#

# @lc code=start


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        temp = ['']*len(s)
        for i in range(len(s)):
            temp[indices[i]] = s[i]

        return ''.join(temp)


# @lc code=end
