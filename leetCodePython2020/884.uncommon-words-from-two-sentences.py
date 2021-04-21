#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#

# @lc code=start

from collections import Counter


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:

        counter = Counter(A.split()+B.split())

        ans = []

        for i, j in counter.items():

            if j < 2:
                ans.append(i)

        return ans


# @lc code=end
