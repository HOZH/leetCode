#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#


class Solution:

    def maxSubArray(self, nums) -> int:

        max_len = len(nums)

        if max_len == 0:
            return 0

        if max_len == 1:
            return nums[0]

        if all(x < 0 for x in nums):
            return max(nums)

        head, tail = 0, max_len - 1

        outter_left, outter_right, answer, left, right = 0, 0, 0, 0, tail

        while True:

            if outter_left + nums[left] >= 0:
                outter_left += nums[left]

            else:

                outter_left = 0

                head = left + 1 if left + 1 < max_len else head

            left += 1

            if outter_right + nums[right] >= 0:
                outter_right += nums[right]

            else:

                outter_right = 0
                tail = right - 1 if right > 0 else tail

            right -= 1

            a = outter_left if outter_left > outter_right else outter_right
            answer = a if a > answer else answer

            if left > right:
                if outter_left + nums[left] < 0 and head != tail:

                    head = left + 1 if left + 1 <= max_len else head

                break

        b = sum(nums[head:tail + 1])
        return b if answer < b else answer
