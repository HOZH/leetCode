#
# @lc app=leetcode id=2094 lang=python3
#
# [2094] Finding 3-Digit Even Numbers
#

# @lc code=start
from itertools import permutations


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        str_digits = [str(i) for i in digits]
        return sorted(list(set(
            map(lambda y: int(''.join(y)), filter(lambda x: x[0] != '0' and int(x[-1]) % 2 == 0, permutations(str_digits, 3))))))

# @lc code=end
