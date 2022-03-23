#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start

from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        c1, c2 = Counter(nums1), Counter(nums2)

        # c3 = c1-c2
        # c4 = c1-c3

        result = []
        # for key, count in c4.items():
        #     result.extend([key]*count)
        for key, count in (c1&c2).items():
            result.extend([key]*count)

        return result


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = {}
        counter2 = {}
        
        def getCount(nums, counter):
            for n in nums:
                if n not in counter:
                    counter[n] = 0
                counter[n]+=1
        
        getCount(nums1, counter1)
        getCount(nums2, counter2)
        
        intersections = {}
        for n in counter2:
            if n in counter1:
                intersections[n] = min(counter1[n], counter2[n])
        ans = []
        for n in intersections:
            while intersections[n]>0:
                ans.append(n)
                intersections[n]-=1
        return ans




# @lc code=end
