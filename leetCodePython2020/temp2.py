from collections import deque, defaultdict


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        hashMap = {}
        stack = []

        for i, n in enumerate(nums):
            while stack and stack[-1][0] < n:
                hashMap[stack.pop()[1]] = n
            stack.append((n, i))

        for i, n in enumerate(nums):
            while stack and stack[-1][0] < n:
                hashMap[stack.pop()[1]] = n
            stack.append((n, i))

        return [hashMap[i] if i in hashMap else -1 for i in range(len(nums))]


"""
[1,2,3,2,1]
[1,2]

[(3, 2), (2, 3), (1, 4)]




"""

"""
 [1,2,3,4,3]

map: key->index, value->next greater number
 [1,2,3] [4,3]

 [x1,x2,x3,' ',3]
[1,2,3,4,3]


[(4,3),(4,3)]

(2,1)



------------
result
(0,2)




"""


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        map = defaultdict(lambda: -1)
        stack = deque()
        length = len(nums)
        count_to_find = len(nums)-nums.count(max(nums))

        for _ in range(2):
            for n in range(length):
                while stack and stack[0][1] < nums[n]:
                    temp = stack.popleft()
                    if temp[0] not in map:
                        map[temp[0]] = nums[n]
                        if len(map) == count_to_find:
                            return [map[x] for x in range(length)]
                stack.appendleft((n, nums[n]))

            if len(map) == count_to_find:
                break

        return [map[x] for x in range(length)]
