#
# @lc app=leetcode id=2011 lang=python3
#
# [2011] Final Value of Variable After Performing Operations
#

# @lc code=start
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:

        result = 0
        for op in operations:
            if op == '++X' or op == 'X++':
                result += 1
            else:
                result -= 1

        return result
# @lc code=end
