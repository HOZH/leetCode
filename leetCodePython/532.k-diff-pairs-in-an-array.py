#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        if k < 0:

            return 0

        num_set, dup_set = set(), set()

        count = 0

        for i in nums:

            if i in num_set:

                dup_set.add(i)

            else:
                num_set.add(i)

        if k == 0:

            return len(dup_set)

        for i in num_set:

            if num_set.__contains__(k+i):

                count += 1

            if num_set.__contains__(i-k):

                count += 1

        return count//2
