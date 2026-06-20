#
# @lc app=leetcode id=3945 lang=python3
#
# [3945] Digit Frequency Score
#

# @lc code=start
from collections import Counter


class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        counter = Counter(str(n))
        return sum(map(lambda x: int(x[0])*x[1], counter.items()))


# @lc code=end
