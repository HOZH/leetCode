#
# @lc app=leetcode id=1304 lang=python3
#
# [1304] Find N Unique Integers Sum up to Zero
#

# @lc code=start


class Solution:
    def sumZero(self, n: int) -> List[int]:

        result = []

        for i in range(1, (n//2)+1):

            result.extend((-i, i))

        return result if n % 2 == 0 else result+[0]


# @lc code=end
