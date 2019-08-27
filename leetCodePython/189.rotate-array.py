#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        dequeue = collections.deque(nums)

        dequeue.rotate(k)

        for i in range(len(dequeue)):

            nums[i] = dequeue[i]
