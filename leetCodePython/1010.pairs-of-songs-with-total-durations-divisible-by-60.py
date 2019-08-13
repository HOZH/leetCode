#
# @lc app=leetcode id=1010 lang=python3
#
# [1010] Pairs of Songs With Total Durations Divisible by 60
#


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        if not time:

            return 0

        helper = [0 for i in range(60)]

        for i in time:
            helper[i % 60] += 1

        result = helper[0]*(helper[0]-1)
        result += helper[30]*(helper[30]-1)

        for i in range(1, 30):
            result += helper[i]*helper[60-i]

        for i in range(31, 60):
            result += helper[i]*helper[60-i]

        result //= 2

        return result
