#
# @lc app=leetcode id=2011 lang=python3
#
# [2011] Final Value of Variable After Performing Operations
#

# @lc code=start
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(list(map(lambda x: -1 if (x in {'--X', 'X--'}) else 1, operations)))

# @lc code=end
