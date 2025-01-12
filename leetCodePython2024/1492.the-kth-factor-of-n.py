#
# @lc app=leetcode id=1492 lang=python3
#
# [1492] The kth Factor of n
#

# @lc code=start
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        counter = 0
        for i in range(1, n+1):
            if n % i == 0:
                counter += 1
            if counter == k:
                return i

        return -1

# @lc code=end
