#
# @lc app=leetcode id=1805 lang=python3
#
# [1805] Number of Different Integers in a String
#

# @lc code=start
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        return len(set(map(lambda x: int(x), filter(lambda x: x != '', ''.join((map(lambda x: x if x.isnumeric() else ' ', [*word]))).split(' ')))))


# @lc code=end
