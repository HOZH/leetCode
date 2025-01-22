#
# @lc app=leetcode id=3300 lang=python3
#
# [3300] Minimum Element After Replacement With Digit Sum
#

# @lc code=start
class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(list(map(lambda x: sum(list(map(lambda y: int(y), [*str(x)]))), nums)))
        
# @lc code=end

