#
# @lc app=leetcode id=961 lang=python3
#
# [961] N-Repeated Element in Size 2N Array
#

# @lc code=start
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:

        encoutered = set()

        for i in A:

            if i in encoutered:
                return i

            encoutered.add(i)

        return -1

# @lc code=end
