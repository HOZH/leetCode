#
# @lc app=leetcode id=829 lang=python3
#
# [829] Consecutive Numbers Sum
#

# @lc code=start


class Solution:
    # (x+x+m-1)*m/2 = N
    # n(n+1)/2
    def consecutiveNumbersSum(self, N: int) -> int:

        count = 0

        for i in range(1, int((N << 1)**.5)+1):

            # temp = (N*2/i - i+1) / 2
            # temp = (2*N - i**2 + i)/2/i
            # if temp > 0 and temp == int(temp):
            #     count += 1
            if (2*N - i**2 + i) % (2*i) == 0:
                count += 1

        return count


# @lc code=end
