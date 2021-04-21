#
# @lc app=leetcode id=1078 lang=python3
#
# [1078] Occurrences After Bigram
#

# @lc code=start

from collections import defaultdict


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        dic = defaultdict(set)
        words = text.split(' ')
        for i in range(len(words)):
            dic[words[i]].add(i)

        ans = []

        for first_index in dic[first]:

            sec_index = first_index+1
            if sec_index in dic[second]:
                if sec_index+1 < len(words):
                    ans.append(words[sec_index+1])

        return ans


# @lc code=end
