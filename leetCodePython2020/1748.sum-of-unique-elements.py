#
# @lc app=leetcode id=1748 lang=python3
#
# [1748] Sum of Unique Elements
#

# @lc code=start
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:

        uni = set()
        encountered = set()

        for i in nums:

            if i not in encountered:
                uni.add(i)
            else:
                if i in uni:
                    uni.remove(i)

            encountered.add(i)

        return sum(uni)


# @lc code=end
