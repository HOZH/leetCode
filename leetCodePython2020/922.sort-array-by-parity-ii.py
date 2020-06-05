#
# @lc app=leetcode id=922 lang=python3
#
# [922] Sort Array By Parity II
#

# @lc code=start


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:

        odds, evens = [], []
        for i in A:
            if i % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)

        result = []
        for i in range(len(A)//2):
            result.append(evens.pop())
            result.append(odds.pop())

        return result

# @lc code=end
