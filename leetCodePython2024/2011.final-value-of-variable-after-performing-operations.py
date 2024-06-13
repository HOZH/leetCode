#
# @lc app=leetcode id=2011 lang=python3
#
# [2011] Final Value of Variable After Performing Operations
#

# @lc code=start
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        answer = 0
        for i in operations:
            if '+' in i:
                answer += 1
            else:
                answer -= 1
        return answer

# @lc code=end
