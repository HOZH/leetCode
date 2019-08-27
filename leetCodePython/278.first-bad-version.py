#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """


        left, right = 1, n

        pivot = (left+right)//2

        first = n

        while left <= right:

            indicator = isBadVersion(pivot)

            if indicator:

                if isBadVersion(pivot-1):

                    right = pivot-1

                else:
                    return pivot

            else:

                if isBadVersion(pivot+1):

                    return pivot+1

                else:

                    left = pivot+1

            pivot = (left+right)//2
