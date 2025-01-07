#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        temp = n
        current = 0
        seen = set()
        while temp != 1:
            seen.add(temp)
            current = 0
            # string = 'abs', [*string]=> ['a','b','c'] [string] => ['abc']
            for i in str(temp):
                current += int(i)**2
            temp = int(current)
            if temp in seen:
                return False
        return True


# @lc code=end
