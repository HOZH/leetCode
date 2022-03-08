#
# @lc app=leetcode id=2164 lang=python3
#
# [2164] Sort Even and Odd Indices Independently
#

# @lc code=start
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evens, odds = [], []
        for i in range(len(nums)):
            if i % 2 == 0:
                evens.append(nums[i])
            else:
                odds.append(nums[i])

        evens.sort()
        odds.sort(reverse=True)

        append_even = True
        result = []
        while len(odds) or len(evens):
            if append_even:
                result.append(evens.pop(0))
            else:
                result.append(odds.pop(0))
            append_even = not append_even
        return result

# @lc code=end
