#
# @lc app=leetcode id=1742 lang=python3
#
# [1742] Maximum Number of Balls in a Box
#

# @lc code=start
from collections import Counter


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:

        temp_container = []
        for i in range(lowLimit, highLimit+1):
            current = i
            temp = 0

            while current > 0:
                temp += current % 10
                current //= 10

            temp_container.append(temp)

        counter = Counter(temp_container)
        return counter.most_common(1)[0][1]


# @lc code=end
