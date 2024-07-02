#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head, end = 0, len(numbers)-1

        while head < end:
            first, sec = numbers[head], numbers[end]
            if first+sec == target:
                return [head+1, end+1]
            elif first+sec < target:
                head += 1
            else:
                end -= 1


# @lc code=end
