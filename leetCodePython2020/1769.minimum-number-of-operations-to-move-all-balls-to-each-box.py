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
        left_count, left_cost, right_count, right_cost = 0, 0, 0, 0

        for i in range(1, length):
            if boxes[i-1] == '1':
                left_count += 1
            left_cost += left_count
            result[i] = left_cost

        for i in range(length-2, -1, -1):
            if boxes[i+1] == '1':
                right_count += 1
            right_cost += right_count
            result[i] += right_cost

        return result

    def minOperations_temp(self, boxes: str) -> List[int]:

        length = len(boxes)
        result = [0]*length

        for i in range(length):

            for j in range(length):
                result[i] += abs(i-j) if boxes[j] == '1' else 0

        return result


# @lc code=end
