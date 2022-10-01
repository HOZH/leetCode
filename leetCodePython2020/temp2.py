# class Solution:
#     def maxSumMinProduct(self, nums: List[int]) -> int:
#         length = len(nums)
#         dp_sum = [[0 for _ in range(length+1)] for _ in range(length+1)]
#         dp_min = [[0 for _ in range(length+1)] for _ in range(length+1)]

#         for i in range(1, length+1):
#             for j in range(1, length+1):
#                 dp_sum[i][j] = dp_sum[i][j-1]+nums[j-1]
#                 dp_min[i][j] = min(dp_min[i][j-1], nums[j-1])
#         # print(dp_sum)
#         # print(dp_min)

#         result = float('-inf')

#         for i in range(len(dp_sum)):
#             for j in range(len(dp_sum[0])):

#                 result = max(dp_sum[i][j], result)

#         return result


# def inorderTraversal(self, root: TreeNode) -> List[int]:

#     bag, visited = deque([root]), []
#     while(len(bag)):
#         current = bag.pop()

#         if current not in visited:
#             visited.append(current.val)
#             if current.right:
#                 bag.append(current.right)
#             if current.left:
#                 bag.append(current.left)

#     print(visited[::])


from collections import Counter
temp = Counter('bracccadabra')

print(temp)
print(temp.keys())
print(temp.items())
