#
# @lc app=leetcode id=1833 lang=python3
#
# [1833] Maximum Ice Cream Bars
#

# @lc code=start
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        costs.sort()

        count = 0

        for i in costs:

            if coins-i >= 0:
                count += 1
                coins -= i
            else:
                break

        return count

# @lc code=end
