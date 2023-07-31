#
# @lc app=leetcode id=2652 lang=python3
#
# [2652] Sum Multiples
#

# @lc code=start
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return sum(list(filter(lambda x:(x%3==0 or x%5 ==0 or x%7==0), range(1,n+1))))
        
# @lc code=end

