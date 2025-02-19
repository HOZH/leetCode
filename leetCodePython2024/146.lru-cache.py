#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.recent_used = OrderedDict()
        self.occupied_len = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.recent_used:
            val = self.recent_used[key]
            del self.recent_used[key]
            self.recent_used[key] = val
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.recent_used:
            del self.recent_used[key]
            self.recent_used[key] = value
        else:
            if self.occupied_len == self.capacity:
                (_removed_key, _) = self.recent_used.popitem(last=False)
            else:
                self.occupied_len += 1

            self.recent_used[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
