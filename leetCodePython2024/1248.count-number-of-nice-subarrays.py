#
# @lc app=leetcode id=1248 lang=python3
#
# [1248] Count Number of Nice Subarrays
#

# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # curr_sum = 0
        # ans = 0
        # prefix_sum = {0: 1} # x times of y odd numbers occured, 1 time of 0 odd number occured

        # for i in range(len(nums)):
        #     curr_sum += nums[i] % 2
        #     # Find subarrays with sum k ending at i
        #     if curr_sum - k in prefix_sum:
        #         ans += prefix_sum[curr_sum - k]

        #     # Increment the current prefix sum in hashmap
        #     prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

        # return ans
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0
        
        for i in range(len(nums)):
            num = nums[i]
            curr += num % 2
            ans += counts[curr - k]
            counts[curr] += 1

        return ans
    


        
# @lc code=end

