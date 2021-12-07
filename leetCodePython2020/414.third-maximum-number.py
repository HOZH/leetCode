#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n, T = list(set(nums)), [float('-inf')]*3
        for i in n:
            if i > T[0]:
                T = [i, T[0], T[1]]
                continue
            if i > T[1]:
                T = [T[0], i, T[1]]
                continue
            if i > T[2]:
                T = [T[0], T[1], i]
        return T[2] if T[2] != float('-inf') else T[0]

# @lc code=end
