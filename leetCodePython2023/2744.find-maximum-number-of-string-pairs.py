#
# @lc app=leetcode id=2744 lang=python3
#
# [2744] Find Maximum Number of String Pairs
#

# @lc code=start
from collections import defaultdict
from math import comb
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        bag = defaultdict(int)
        for i in words:
            if i<i[::-1]:
                bag[i]+=1
            else:
                bag[i[::-1]]+=1
        result = 0
        for key in bag.keys():
            result += comb(bag[key],2)

        return result

        
# @lc code=end

