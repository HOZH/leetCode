#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start


class Node:
    def __init__(self, start, end, value=float('-inf')):
        self.start = start
        self.end = end
        self.value = value
        self.left = None
        self.right = None


class Solution:
    # def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
    #     if len(nums) < k:
    #         return []
    #     # dp[i]= max value within interval i~i+k
    #     dp = [0] * (len(nums) - k + 1)
    #     dp[0] = max(nums[:k])
    #     for i in range(1, len(nums) - k + 1):
    #         dp[i] = max(nums[i:i + k]) if dp[i - 1] == nums[i -
    #                                                         1] else max(nums[i + k - 1], dp[i - 1])
    #     return dp
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        def build_tree(node):
            if node:
                if node.start != node.end:
                    m = (node.start + node.end) // 2
                    node.left = build_tree(Node(node.start, m))
                    node.right = build_tree(Node(m + 1, node.end))
                    node.value = max(float('-inf') if not node.left else node.left.value,
                                     float('-inf') if not node.right else node.right.value)
                else:
                    node.value = nums[node.start]
            return node

        # def preorder(node):
        #     if node:
        #         print([node.start, node.end, node.value])
        #         preorder(node.left)
        #         preorder(node.right)

        def get_value(node, start, end):

            if node.start == start and node.end == end:
                return node.value

            if end <= node.left.end:
                return get_value(node.left, start, end)
            elif start >= node.right.start:
                return get_value(node.right, start, end)

            else:
                return max(get_value(node.left, start, node.left.end), get_value(node.right, node.left.end + 1, end))

        root = build_tree(Node(0, len(nums) - 1))

        dp = [0] * (len(nums) - k + 1)
        dp[0] = get_value(root, 0, k - 1)
        for i in range(1, len(nums) - k + 1):
            dp[i] = get_value(root, i, i + k - 1) if dp[i - 1] == nums[i -
                                                                       1] else max(nums[i + k - 1], dp[i - 1])
        return dp


# @lc code=end
