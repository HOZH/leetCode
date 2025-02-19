#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start

class MonotonicQueue:

    def push(self, e):
        while len(self.data_) and e > self.data_[-1]:
            self.data_.pop()
        self.data_.append(e)

    def pop(self):
        self.data_.popleft()

    def max(self):

        return self.data_[0]

    def __init__(self):

        self.data_ = deque()

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = MonotonicQueue()
        ans = []

        for i in range(len(nums)):
            q.push(nums[i])

            if i-k+1 >= 0:
                ans.append(q.max())
                if nums[i-k+1] == q.max():
                    q.pop()

        return ans
        
# @lc code=end

