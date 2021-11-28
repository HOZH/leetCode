#
# @lc app=leetcode id=760 lang=python3
#
# [760] Find Anagram Mappings
#

# @lc code=start
class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:

        used = set()
        ans = []

        for i in nums1:
            starting_index = 0
            while True:
                current = nums2.index(i, starting_index)
                if current in used:
                    starting_index = current+1
                else:
                    used.add(current)
                    ans.append(current)
                    break
        return ans

# @lc code=end
