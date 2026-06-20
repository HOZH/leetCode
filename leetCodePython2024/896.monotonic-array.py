#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        '''
        Ex 1:
        nums = [1,2,2,3]
        Output: true


        Example 2:
        Input: nums = [6,5,4,4]
        Output: true


        Example 3:
        Input: nums = [1,3,2]
        Output: false
        '''
        is_inc = True
        is_desc = True
        inc_index = 0
        desc_indx = 0 
        prev = nums[0]
        increasing_list = [prev]
 
        num_length = len(nums)
        for index in range(1,num_length):
            current = nums[index]
            if current>=prev:
                increasing_list.append(current)
                inc_index += 1
                prev = current
            else:
                is_inc = False
                break
        if len(increasing_list) == num_length:
            print(len(increasing_list) == num_length)
            return True
        
        decreasing_list = []
        prev = nums[0]
        for index in range(1, num_length):
            current = nums[index]
            if current <= prev:
                decreasing_list.append(current)
                prev = current
            else:
                break
        if len(decreasing_list) == num_length:
            print(len(decreasing_list) == num_length)

            return True
        
        return False
            
        
# @lc code=end

def isMonotonic(self, nums: List[int]) -> bool:
        i = 1
        prev = nums[0]
        incr_index = 1
        while i < len(nums):
            curr = nums[i]
            if curr >= prev:
                incr_index += 1
                prev = curr
                i += 1
            else:
                break
 
        if incr_index == len(nums):
            return True
        
        desc_index = 1
        j = 1
        prev = nums[0]
        while j < len(nums):
            curr = nums[j]
            if curr <= prev:
                desc_index += 1
                prev = curr
            j += 1
    
        if desc_index == len(nums):
            return True
       
        return False