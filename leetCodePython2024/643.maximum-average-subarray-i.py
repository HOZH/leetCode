#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = sum(nums[:k])
        current = result

        for i in range(len(nums)-k):
            current = current-nums[i]+nums[i+k]
            # if current> result:
            #      result = current
            # else:
            #      result = result
            result = max(result, current)

        return result/k


# @lc code=end

def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]

        i = 0
        j = k
        max_avg = float('-inf')

        while j <= len(nums):
            window = nums[i:j]
            curr_avg = sum(window) / k
            max_avg = max(curr_avg, max_avg)

            i += 1
            j += 1
        return max_avg


