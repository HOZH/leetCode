#
# @lc app=leetcode id=1614 lang=python3
#
# [1614] Maximum Nesting Depth of the Parentheses
#

# @lc code=start

from collections import deque


class Solution:
    def maxDepth(self, s: str) -> int:

        # s = ''.join(list(filter(lambda x: x == '(' or x == ')', s)))
        l = 0
        ans = 0
        for i in s:
            if i == '(':
                l += 1
            elif i == ')':
                l -= 1

            ans = max(ans, l)

        return ans

    def maxDepth_temp(self, s: str) -> int:

        l_stack, r_stack = deque(), deque()

        ans = 0
        sub_max_depth = 0

        for i in range(len(s)):

            if s[i] == '(':
                l_stack.appendleft(i)
            elif s[i] == ')':
                r_stack.appendleft(i)

            current_l_cap, current_r_cap = len(l_stack), len(r_stack)

            if current_l_cap and current_r_cap:

                # if current_r_cap <= current_l_cap:

                l, r = l_stack.popleft(), r_stack.popleft()

                temp_sub = 1+self.maxDepth(s[l+1:r])

                sub_max_depth = sub_max_depth if sub_max_depth > temp_sub else temp_sub

        ans += sub_max_depth

        return ans


# @lc code=end
