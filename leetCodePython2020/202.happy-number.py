#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        temp = str(n)

        while temp != '1':
            if len(temp) > 1:
                temp = str(sum(map(lambda x: int(x)**2, [*temp])))
            else:
                temp = str(int(temp)**2)
            if temp in seen:
                return False

            seen.add(temp)
        return True


# @lc code=end
