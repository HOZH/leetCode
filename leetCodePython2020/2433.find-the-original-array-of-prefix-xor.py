#
# @lc app=leetcode id=2433 lang=python3
#
# [2433] Find The Original Array of Prefix Xor
#

# @lc code=start
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return [pref[0]]+[pref[i] ^ pref[i-1]for i in range(1, len(pref))]

# @lc code=end
