#
# @lc app=leetcode id=1769 lang=python3
#
# [1769] Minimum Number of Operations to Move All Balls to Each Box
#

# @lc code=start
from functools import reduce


class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        length = len(boxes)
        result = [0]*length

        for i in range(length):

            for j in range(length):
                result[i] += abs(i-j) if boxes[j] == '1' else 0

        return result


# @lc code=end
