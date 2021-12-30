#
# @lc app=leetcode id=359 lang=python3
#
# [359] Logger Rate Limiter
#

# @lc code=start
class Logger:

    def __init__(self):
        self.bag = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.bag:
            self.bag[message] = timestamp
            return True

        if timestamp < self.bag[message]+10:
            return False
        else:
            self.bag[message] = timestamp
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
# @lc code=end
