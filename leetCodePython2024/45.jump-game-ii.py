#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start


class Solution:
    def jump_wrong(self, nums: List[int]):
        lastPos = len(nums) - 1
        change_indices = []

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= lastPos:
                change_indices.append(i)
                lastPos = i
        # [0,1,2,3] => [0,3] => len(change_indices)+1
        change_indices = change_indices[::-1]

        consolidated_indices = []
        prev_max_index = 0
        for i in change_indices:
            if len(consolidated_indices) == 0 or i > prev_max_index:
                consolidated_indices.append(i)
                prev_max_index = i+nums[i]

        print(change_indices)
        print(consolidated_indices)
        return len(consolidated_indices)
   
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        # jumps: Total number of jumps made.
        # currentEnd: The farthest index we can reach with the 'jumps' we've already taken.
        # farthest: The absolute farthest index we can reach from ANY position visited so far.
        jumps, currentEnd, farthest = 0, 0, 0
        for i in range(len(nums) - 1):
            # max index we can reach from current index i
            farthest = max(farthest, i + nums[i])
            # if current index i is not less than the max index we can reach from previous jump
            if i >= currentEnd:
                jumps += 1
                # update the max index we can reach from current jump to the farthest index
                # we visited so far
                currentEnd = farthest
            if currentEnd >= len(nums)-1:
                return jumps  
            
        # [2, 3, 1, 1, 4]
        # i = 0 jumps = 1,currentEnd = 0, farthest = 2, i >= currentEnd = 1>=0 = true, then currentEnd = 2, jumps=1
        # i = 1 jumps = 1,currentEnd = 2, farthest = 5, i >= currentEnd = 1>=2 = false, then currentEnd = 2, jumps=1
        # i = 2 jumps = 2, currentEnd = 2, farthest = 5, i >= currentEnd = 2>=2 = true, then currentEnd = 5, jumps=2
        # return


        

              
        
        
# @lc code=end

