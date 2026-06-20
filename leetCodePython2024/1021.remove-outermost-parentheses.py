#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ''
        left_count, right_count = 0, 0
        current_sub_str = ''

        for i in s:
            if i == '(':
                left_count += 1
            elif i == ')':
                right_count += 1
            current_sub_str += i

            if left_count == right_count:
                ans += current_sub_str[1:-1]
                current_sub_str = ''

        return ans


# @lc code=end

from collections import deque
a = deque()
a.popleft()
a.pop()
def removeOuterParentheses(self, s: str) -> str:
        stack = []
        # when stack is empty, add to the string 
        output = ""

        for paran in s:
            if paran == "(":
                stack.append(paran)
            else:
                # if stack[-1] == "(":
                stack.pop()
                if len(stack) > 0:
                    output += "()"

        return output
(()
(
()
['(', '(']

[('(, 0'), ('(', 1)]

if stack is empty:
    0, curr_index -> 0,5

s =
"( ( ) ( ) )  (())  ( () (()) )"
[6, ] -> 5, 0
string[0 + 1:5]

stack = (())
 ()()()() (())
Output
"()()()()     ()()"

Expected
"()()()()  (())"