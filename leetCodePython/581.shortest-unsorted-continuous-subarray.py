#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        length = len(nums)

        if length == 0:
            return 0

        left, right = 0, length - 1

        temp_arr = nums[:]
        temp_arr.sort()

        left_ready, right_ready = False, False

        while True:

            if nums[left] == temp_arr[left]:

                left += 1

            else:
                left_ready = True

            if nums[right] == temp_arr[right]:

                right -= 1

            else:

                right_ready = True

            if left >= right:
                return 0
            elif right_ready and left_ready:
                break

        return right - left + 1
