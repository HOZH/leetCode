#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
from collections import deque


class Solution:

    def nextGreaterElement_temp1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = {}
        stack = deque()
        for n in nums2:
            while stack and stack[0] < n:
                map[stack.popleft()] = n
            stack.appendleft(n)

        return [-1 if n not in map else map[n] for n in nums1]

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indexes = []
        ans = []

        found = dict()
        index_dict = dict()

        for i in nums1:
            index_dict[i] = nums2.index(i)
            found[index_dict[i]] = -1

        indexes = sorted(list(index_dict.values()))  # [0,2,4,5]l

        temp_set = set()
        temp_set.add(indexes[0])

        i = indexes[0]+1  # 1
        indexes = indexes[1:]

        current_index = 0

        while i < (len(nums2)):
            if current_index<len(indexes) and indexes[current_index] == i:
                temp_set.add(i)
                current_index+=1
                # indexes = indexes[1:]

            removing = set()
            for j in temp_set:
                if nums2[i] > nums2[j]:
                    found[j] = nums2[i]
                    removing.add(j)

            temp_set -= removing

            i += 1

        ans = []
        for i in nums1:
            ans.append(found[index_dict[i]])

        return ans



    def nextGreaterElement_temp(self, nums1: List[int], nums2: List[int]) -> List[int]:

        indexs = []
        ans = []

        for i in nums1:
            indexs.append(nums2.index(i))

        for i in indexs:
            current = nums2[i]
            found = False
            for j in range(i+1, len(nums2)):
                if nums2[j] > current:
                    ans.append(nums2[j])
                    found = True
                    break
            if not found:
                ans += [-1]

        return ans


# @lc code=end
