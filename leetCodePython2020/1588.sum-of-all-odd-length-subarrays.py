#
# @lc app=leetcode id=1588 lang=python3
#
# [1588] Sum of All Odd Length Subarrays
#

# @lc code=start


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        count = 0
        length = len(arr)
        result = 0
        for i in range(0, length):
            for j in range(i+1, length):
                if (i-j) % 2 == 0:
                    result += sum(arr[i:j+1])

        return result+sum(arr)

# @lc code=end
