#
# @lc app=leetcode id=1475 lang=python3
#
# [1475] Final Prices With a Special Discount in a Shop
#

# @lc code=start


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        final_prices = [0] * len(prices)

        for i in range(len(prices)):
            found = False

            for j in range(i+1, len(prices)):

                if prices[j] <= prices[i]:

                    final_prices[i] = prices[i]-prices[j]
                    found = True
                    break

            if not found:
                final_prices[i] = prices[i]

        return final_prices


# @lc code=end
