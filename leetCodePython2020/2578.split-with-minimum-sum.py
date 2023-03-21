#
# @lc app=leetcode id=2578 lang=python3
#
# [2578] Split With Minimum Sum
#

# @lc code=start
class Solution:
    def splitNum(self, num: int) -> int:

        nums = sorted(list(map(lambda x: int(x), [*str(num)])))

        num1, num2 = 0, 0
        flag = True

        for i in nums:
            if flag:
                num1 *= 10
                num1 += i
            else:
                num2 *= 10
                num2 += i
            flag = not flag

        return num1+num2


# @lc code=end
