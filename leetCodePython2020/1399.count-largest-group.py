#
# @lc app=leetcode id=1399 lang=python3
#
# [1399] Count Largest Group
#

# @lc code=start
from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:

        temp_dict = defaultdict(list)
        for i in range(1, n+1):
            current = str(i)
            current_val = 0
            for j in current:
                current_val += int(j)

            temp_dict[current_val].append(i)

        bag = list(temp_dict.values())

        bag.sort(key=lambda x: len(x), reverse=True)

        max_len = len(bag[0])

        ans = 0

        for i in bag:
            if len(i) == max_len:
                ans += 1
            else:
                break
        return ans

# @lc code=end
