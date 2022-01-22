#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#

# @lc code=start


class StockSpanner_temp:

    def __init__(self):

        self.arr = []
        self.dp = []

    def next(self, price: int) -> int:

        self.arr.append(price)
        count = 1
        i = len(self.arr)-2

        while i >= 0:
            if self.arr[i] <= price:
                count += self.dp[i]
                i -= self.dp[i]
            else:
                break

        self.dp.append(count)
        return count


class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        ans = 1
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]
        self.stack.append((price, ans))

        return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end
