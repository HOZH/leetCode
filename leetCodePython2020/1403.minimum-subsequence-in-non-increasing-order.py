#
# @lc app=leetcode id=1403 lang=python3
#
# [1403] Minimum Subsequence in Non-Increasing Order
#

# @lc code=start
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:

        total = sum(nums)
        temp_arr = sorted(nums, reverse=True)
        temp_result = []
        temp = 0

        for i in range(len(temp_arr)):

            temp_result.append(temp_arr[i])
            temp += temp_arr[i]

            if temp > total-temp:
                break

        return temp_result
        # result = []

        # for i in nums:
        #     print(i)
        #     if i in temp_result:
        #         result.append(i)
        # return result


# @lc code=end
