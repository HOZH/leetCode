#
# @lc app=leetcode id=1370 lang=python3
#
# [1370] Increasing Decreasing String
#

# @lc code=start

from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:

        counter = Counter(s)
        keys = sorted(counter.keys())
        result = ''
        while counter.most_common(1)[0][1]:

            for i in range(len(keys)):

                if counter[keys[i]] != 0:
                    result += keys[i]
                    counter[keys[i]] -= 1

            for i in range(len(keys)-1, -1, -1):

                if counter[keys[i]] != 0:
                    result += keys[i]
                    counter[keys[i]] -= 1

        return result

# @lc code=end
