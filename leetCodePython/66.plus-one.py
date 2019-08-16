#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        length = len(digits)
        if length == 0:
            return [1]

        digits[-1] += 1

        for i in range(length-1, -1, -1):

            if digits[i] == 10:
                digits[i] = 0

                if i-1 != -1:
                    digits[i-1] += 1

                else:
                    digits.insert(0, 1)

        return digits
