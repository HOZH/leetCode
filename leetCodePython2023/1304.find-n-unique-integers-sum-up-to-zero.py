#
# @lc app=leetcode id=1304 lang=python3
#
# [1304] Find N Unique Integers Sum up to Zero
#

# @lc code=start
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range(1, (n//2)+1):
            ans.append(i)
            ans.append(0-i)
        if n % 2 == 0:
            return ans
        else:
            return ans+[0]


# @lc code=end
