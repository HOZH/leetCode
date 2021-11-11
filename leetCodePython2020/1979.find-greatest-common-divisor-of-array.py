#
# @lc app=leetcode id=1979 lang=python3
#
# [1979] Find Greatest Common Divisor of Array
#

# @lc code=start
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        head,tail = nums[0],nums[-1]

        def gcd(a,b):

            if b==0:
                return a
            return gcd(b,a%b)
        
        return gcd(head,tail)
        
# @lc code=end

