#
# @lc app=leetcode id=1323 lang=python3
#
# [1323] Maximum 69 Number
#

# @lc code=start
class Solution:
    def maximum69Number(self, num: int) -> int:
        num_list = [int(i) for i in [*str(num)]]
        for i in range(0, len(num_list)):
            if num_list[i] == 6:
                num_list[i] = 9
                break

        ans = 0
        for i in num_list:
            ans *= 10
            ans += i
        return ans


# @lc code=end
