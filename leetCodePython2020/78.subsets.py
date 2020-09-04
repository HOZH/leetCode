#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # self.ans = []
        # nums.sort()

        # def c(target_count, depth, start_index, current_list):
        #     if target_count == depth:
        #         self.ans.append(current_list)
        #     for i in range(start_index, len(nums)):
        #         c(target_count, depth+1, i+1, current_list+[nums[i]])

        # for i in range(len(nums)+1):
        #     c(i, 0, 0, [])
        # return self.ans
        self.ans = []
        s = 1 << (len(nums)+1)
        s -= 1
        for i in range(2**len(nums)):
            current = []
            for j in range(len(nums)):
                # jth of i is 1 in binary
                if i & 1 << j:
                    current.append(nums[j])
            self.ans.append(current)
        return self.ans


# @lc code=end
