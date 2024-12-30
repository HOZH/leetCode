#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
from decimal import Decimal


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return x**n
        def helper(local_x, local_n):
            if local_n == 0:
                return 1
            if local_n < 0:
                return 1/helper(local_x, -local_n)
            return local_x*helper(local_x, local_n-1)

        count_for_batch_division = 1
        new_n_for_small_batch = n

        while abs(new_n_for_small_batch) > 500:
            new_n_for_small_batch = new_n_for_small_batch//2
            count_for_batch_division *= 2
        ans = helper(
            Decimal(x), new_n_for_small_batch) ** count_for_batch_division
        if abs(n) > 500:
            addtional_factor = n-count_for_batch_division*new_n_for_small_batch
            add_up = Decimal((x))**addtional_factor
            ans *= add_up

        return ans

# @lc code=end
