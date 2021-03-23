#
# @lc app=leetcode id=933 lang=python3
#
# [933] Number of Recent Calls
#

# @lc code=start
class RecentCounter:

    def __init__(self):

        # self.prev = None
        # self.prev_3001 = [0] * 3001
        # self.prev_sum = 0
        self.calls = []

    def ping(self, t: int) -> int:

        self.calls.append(t)

        while self.calls[0] < t-3000:
            self.calls.pop(0)

        return len(self.calls)

        # last_request_time = self.prev or -9999999999
        # prev_ddl = t - 3000
        # self.prev = t

        # if t == last_request_time:
        #     self.prev_3001[-1] += 1
        #     self.prev_sum += 1

        # elif prev_ddl > last_request_time:
        #     self.prev_3001 = [0] * 3000 + [1]
        #     self.prev_sum = 1

        # else:
        #     diff = t - last_request_time

        #     temp = self.prev_3001[diff:]

        #     self.prev_sum = sum(temp)+1

        #     self.prev_3001 = temp + [0] * (diff - 1) + [1]

        # return self.prev_sum

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end
