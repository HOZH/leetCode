#
# @lc app=leetcode id=2033 lang=python3
#
# [2033] Minimum Operations to Make a Uni-Value Grid
#

# @lc code=start
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = [item for sublist in grid for item in sublist]
        arr.sort()
        placeholder1 = arr[len(arr)//2]
        # placeholder2 = arr[len(arr)//2-1]

        def helper(target):
            count = 0 
            for i in arr:
                current =abs(target-i)/x
                if current != int(current):
                    return -1
                count+=current
            return count

        result1 = helper(placeholder1)
        # result2 = helper(placeholder2)
        # if result1 == result2 == -1:
        #     return -1
        return int(result1)
        # return int(min(result1,result2))


# @lc code=end

