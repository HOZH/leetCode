#
# @lc app=leetcode id=3541 lang=python3
#
# [3541] Find Most Frequent Vowel and Consonant
#

# @lc code=start
from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        counter = Counter(s)
        ans = max(
            counter['a'], counter['e'], counter['i'], counter['o'], counter['u'])
        del counter['a']
        del counter['e']
        del counter['i']
        del counter['o']
        del counter['u']

        if len(counter.keys()) == 0:
            return ans

        return ans+max(counter.values())


# @lc code=end
