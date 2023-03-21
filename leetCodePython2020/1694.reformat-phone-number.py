#
# @lc app=leetcode id=1694 lang=python3
#
# [1694] Reformat Phone Number
#

# @lc code=start
class Solution:
    def reformatNumber(self, number: str) -> str:
        arr = list(filter(lambda x: x != ' ' and x != '-', [*number]))

        ans = ''
        for i in range(0, len(arr)//3*3, 3):
            ans += ''.join(arr[i:i+3])
            ans += '-'

        remainder = len(arr) % 3
        # case 3 digits
        if remainder % 3 == 0:
            ans = ans[:-1]
        # case 4 digits
        elif remainder % 3 == 1:
            ans = ans[:-2]
            ans += '-'+arr[-2]+arr[-1]
        # case 2 digits
        else:
            ans += arr[-2]+arr[-1]

        return ans


# @lc code=end
