#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        length = len(nums)

        if length < 3:
            return True

        first_time = True

        prev = nums[0]

        for i in range(1, length):

            if nums[i] < prev:

                if first_time:

                    first_time = False

                    temp_key = True

                    for j in range(i - 1):

                        if nums[j] > nums[i]:
                            temp_key = False
                            break

                    if temp_key:

                        nums[i - 1] = nums[i]

                    else:
                        nums[i] = prev
                        continue

                else:

                    return False

            prev = nums[i]

        return True
