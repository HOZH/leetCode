#
# @lc app=leetcode id=1588 lang=python3
#
# [1588] Sum of All Odd Length Subarrays
#

# @lc code=start
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        length = len(arr)
        for i in range(length):
            for j in range(i, length):
                if (i-j) % 2 == 0:
                    ans += sum(arr[i:j+1])

        return ans


# @lc code=end
