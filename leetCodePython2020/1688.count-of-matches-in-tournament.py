#
# @lc app=leetcode id=1688 lang=python3
#
# [1688] Count of Matches in Tournament
#

# @lc code=start
class Solution:
    def numberOfMatches(self, n: int) -> int:

        count = 0

        while n > 1:

            if n % 2 == 0:
                count += n/2
                n /= 2
            else:
                count += (n-1)/2
                n //= 2
                n += 1

        return int(count)


# @lc code=end
