#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#

# @lc code=start
class Solution:
    def diffWaysToCompute(self, expression):
        # no negative numbers given
        if not len(expression):
            return [0]
        nums_and_operators = []
        prev = expression[0]
        for i in range(1, len(expression)):
            current = expression[i]
            is_current_numeric = current.isdigit()
            if is_current_numeric:
                if prev.isdigit():
                    prev += current
                else:
                    nums_and_operators.append(prev)
                    prev = current
            else:
                nums_and_operators.append(prev)
                prev = current

        nums_and_operators.append(prev)

        self.ops = {'+', '-', '*'}

        def get_operation_result(num1, num2, op):
            match op:
                case '+':
                    return num1 + num2
                case '-':
                    return num1 - num2
                case '*':
                    return num1 * num2

        def helper(local_nums_and_operators):
            if len(local_nums_and_operators) == 1:
                return [int(local_nums_and_operators[0])]
            ans = []
            for i in range(len(local_nums_and_operators)):
                current = local_nums_and_operators[i]
                if current in self.ops:
                    left_local_result = helper(local_nums_and_operators[:i])
                    right_local_result = helper(
                        local_nums_and_operators[i + 1:])
                    for left in left_local_result:
                        for right in right_local_result:
                            ans.append(get_operation_result(
                                left, right, current))
            return ans

        return helper(nums_and_operators)


# @lc code=end
