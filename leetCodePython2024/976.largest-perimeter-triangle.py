#
# @lc app=leetcode id=976 lang=python3
#
# [976] Largest Perimeter Triangle
#

# @lc code=start
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        index = len(nums)-1
        a = b = c = 0
        answer = 0

        while index-2 >= 0:
            a = nums[index]
            b = nums[index-1]
            c = nums[index-2]
            index -= 1
            if a >= b+c:
                continue
            elif answer == 0:
                return a+b+c

        return 0
            



        
# @lc code=end

[1,2,1,10]
a+b > c

1, 2, 1
a, b, c

a + b = 3 > 1
a + c = 2 > 2 # fails
b + c = 3 > 1

    def largestPerimeter(self, nums: List[int]) -> int:
        result = 0

        nums.sort()

        i = len(nums) - 1

        while i >= 0:
            a = nums[i]
            b = nums[i - 1]
            c = nums[i - 2]
            if a + b > c and a + c > b and b + c > a:
                return a + b + c
            i -= 1

        return result