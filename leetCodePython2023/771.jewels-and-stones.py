#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set([*jewels])
        ans = 0
        for i in stones:
            if i in jewels:
                ans += 1

        return ans

# @lc code=end
