#
# @lc app=leetcode id=556 lang=python3
#
# [556] Next Greater Element III
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # Step 1: Convert number to a list of digits
        digits = list(map(int, str(n)))
        l = len(digits)

        # Step 2: Find the pivot (first decreasing element from the right)
        i = l - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        # If no pivot found, no next greater number can be formed
        if i < 0:
            return -1

        # Step 3: Find the smallest digit larger than digits[i]
        j = l - 1
        while digits[j] <= digits[i]:
            j -= 1

        # Step 4: Swap digits[i] with digits[j]
        digits[i], digits[j] = digits[j], digits[i]

        # Step 5: Reverse the digits after the pivot
        digits[i + 1:] = reversed(digits[i + 1:])

        # Step 6: Convert back to integer and check for overflow
        next_n = int(''.join(map(str, digits)))
        return next_n if next_n < 2**31 else -1


# @lc code=end
