
#
# @lc app=leetcode id=3838 lang=python3
#
# [3838] Weighted Word Mapping
#

# @lc code=start
from functools import reduce


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result_mapping = [chr(i) for i in range(122, 96, -1)]

        def helper(w):
            return result_mapping[sum(map(lambda x: weights[ord(x)-97], w)) % 26]

        return ''.join(list(map(lambda x: helper(x), words)))


# @lc code=end
