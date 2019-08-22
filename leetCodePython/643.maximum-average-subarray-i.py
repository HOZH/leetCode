#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        result = sum(nums[0:k])
        current = result

        for i in range(0, len(nums)-k):
            current += nums[i+k]-nums[i]

            if current > result:

                result = current

        return result/k
