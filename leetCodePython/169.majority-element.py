#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#


from functools import reduce
class Solution:

    #duno why mine is much slowly when used two similar approach from smaple code
    def majorityElement(self, nums: List[int]) -> int:
        #     nums.sort()
        #     return(nums[len(nums)//2])

        dic = dict()

        for i in nums:

            if i in dic:

                dic[i] += 1

            else:
                dic[i] = 1

        return reduce(lambda x, y: x if x[1] > y[1] else y, list(dic.items()))[0]




        

