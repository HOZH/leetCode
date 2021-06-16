#
# @lc app=leetcode id=1442 lang=python3
#
# [1442] Count Triplets That Can Form Two Arrays of Equal XOR
#

# @lc code=start


class Solution:
  def countTriplets(self, A: List[int]) -> int:
    X = [0] + list(accumulate(A, xor))
    n = len(X)
    res = 0
    for i in range(1, n):
      for k in range(i+1, n):
        if X[i-1] == X[k]:
          res += k-i
    return res
# @lc code=end

