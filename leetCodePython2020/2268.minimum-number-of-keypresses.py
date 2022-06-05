#
# @lc app=leetcode id=2268 lang=python3
#
# [2268] Minimum Number of Keypresses
#

# @lc code=start
from collections import Counter


class Solution:
    def minimumKeypresses(self, s: str) -> int:

        counter = Counter(s)
        most_common_index = 1
        result = 0
        for count in sorted(list(counter.values()), reverse=True):
            result += (most_common_index//9 +
                       (0 if most_common_index % 9 == 0 else 1))*count
            most_common_index += 1
        return result


# @lc code=end
