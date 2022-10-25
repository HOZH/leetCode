#
# @lc app=leetcode id=2283 lang=python3
#
# [2283] Check if Number Has Equal Digit Count and Digit Value
#

# @lc code=start
class Solution:
    def digitCount(self, num: str) -> bool:
        counter = {}
        for i in range(len(num)):
            counter[str(i)] = int(num[i])

        return all([num.count(i) == counter[i] for i in counter.keys()])

# @lc code=end
