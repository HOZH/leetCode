#
# @lc app=leetcode id=726 lang=python3
#
# [726] Number of Atoms
#

# @lc code=start

from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:

        self.formula = formula

        def helper(start):

            current_counter = Counter()
            c = 1

            current_index = start

            # TODO create a dict to hold local counts of local eles
            current_ele = ''
            current_count = -1
            while current_index < len(self.formula):

                # TODO find the cloest () and pass it to the deep level, the interal of that should be ignored in this for loop

                # completing name for current ele
                if ord(self.formula[current_index]) in range(97, 123):
                    current_ele += self.formula[current_index]
                    current_index += 1

                # starting of new ele
                elif ord(self.formula[current_index]) in range(65, 91):

                    if current_ele != '':
                        current_counter[current_ele] += current_count if current_count > 0 else 1
                    current_ele = self.formula[current_index]
                    current_count = -1
                    current_index += 1

                # modify the count of current ele
                elif ord(self.formula[current_index]) in range(48, 58):
                    # leading digit of count
                    if current_count == -1:
                        current_count = int(self.formula[current_index])
                    else:
                        current_count *= 10
                        current_count += int(self.formula[current_index])

                    current_index += 1

                elif self.formula[current_index] == '(':

                    current_counter[current_ele] += current_count if current_count > 0 else 1
                    current_count = -1
                    current_ele = ''

                    current_index += 1

                    sub_counter = helper(current_index)
                    current_counter = current_counter+sub_counter[0]
                    current_index = sub_counter[1]

                elif self.formula[current_index] == ')':
                    # todo seek for ratio and call the rec function

                    current_index += 1

                    c = ''
                    while current_index < len(self.formula):
                        if self.formula[current_index].isnumeric():
                            c += self.formula[current_index]
                            current_index += 1
                        else:
                            break
                    c = 1 if c == '' else int(c)

                    current_index -= 1
                    break

            current_counter[current_ele] += current_count if current_count > 0 else 1
            for j in current_counter.keys():
                current_counter[j] = current_counter[j] * c

            return current_counter, current_index + 1

        temp_result = helper(0)[0]
        temp_result_keys = temp_result.keys()
        result = ''
        for i in sorted(temp_result_keys):
            if i != '':
                result += i
                result += '' if temp_result[i] == 1 else str(temp_result[i])
        return result
        # @lc code=end
