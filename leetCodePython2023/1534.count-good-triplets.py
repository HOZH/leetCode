#
# @lc app=leetcode id=1534 lang=python3
#
# [1534] Count Good Triplets
#

# @lc code=start
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        cnt = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if abs(arr[i]-arr[j]) <= a and abs(arr[k]-arr[j]) <= b and abs(arr[i]-arr[k]) <= c:
                        cnt += 1
        return cnt

# @lc code=end
