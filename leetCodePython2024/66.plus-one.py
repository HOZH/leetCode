#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] = (digits[-1]+1) if digits[-1] != 9 else 0
        add_one_to_next_digit = True if digits[-1] == 0 else False

        for i in range(len(digits)-2, -1, -1):
            temp = digits[i]
            if add_one_to_next_digit:
                temp += 1
            if temp == 10:
                temp = 0
                add_one_to_next_digit = True
            else:
                add_one_to_next_digit = False
            digits[i] = temp

        if digits[0] == 0:
            return [1]+digits
        return digits


# @lc code=end
