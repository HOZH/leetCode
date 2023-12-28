#
# @lc app=leetcode id=1475 lang=python3
#
# [1475] Final Prices With a Special Discount in a Shop
#

# @lc code=start

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        ans = deque([prices[-1]])

        for i in range(len(prices)-2, -1, -1):
            original_price = prices[i]
            found_discount = False
            for j in range(i+1,len(prices)):
                if prices[j] <= original_price:
                    ans.appendleft(original_price-prices[j])
                    found_discount = True
                    break
            if not found_discount:
                ans.appendleft(original_price)

        return ans


# @lc code=end
