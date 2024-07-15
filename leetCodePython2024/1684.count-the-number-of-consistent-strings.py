#
# @lc app=leetcode id=1684 lang=python3
#
# [1684] Count the Number of Consistent Strings
#

# @lc code=start
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        allowed = set([*allowed])
        ans = 0
        for i in words:
            if all([True if j in allowed else False for j in i]):
                ans += 1

        return ans

# @lc code=end
