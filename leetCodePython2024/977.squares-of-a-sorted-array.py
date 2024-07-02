#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        begin_index_for_zero_or_above = 10**4
        for i in range(len(nums)):
            if nums[i] >= 0:
                begin_index_for_zero_or_above = i
                break

        negative_nums = nums[:begin_index_for_zero_or_above][::-1]
        rest_nums = nums[begin_index_for_zero_or_above:]
        ans = []

        while len(negative_nums) and len(rest_nums):
            sq_negative_num, sq_rest_num = negative_nums[0]**2, rest_nums[0]**2
            if sq_negative_num <= sq_rest_num:
                ans.append(sq_negative_num)
                negative_nums = negative_nums[1:]
            else:
                ans.append(sq_rest_num)
                rest_nums = rest_nums[1:]

        if len(negative_nums):
            ans.extend([i**2 for i in negative_nums])
        elif len(rest_nums):
            ans.extend([i**2 for i in rest_nums])

        return ans


# @lc code=end
