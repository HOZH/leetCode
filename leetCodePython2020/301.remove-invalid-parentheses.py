#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#

# @lc code=start


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        self.ans = []
        self.not_letters = set()

        @lru_cache(None)
        def is_valid(temp):
            left, right = 0, 0
            for i in range(len(temp)):
                if temp[i] == '(':
                    left += 1
                elif temp[i] == ')':
                    right += 1
                if right > left:
                    return False
            return True if left == right else False

        # def c(nums, target_count, depth, start_index, current_list, ans):
        #     if target_count == depth:
        #         ans.append(set(current_list))
        #         return
        #     for i in range(start_index, len(nums)):
        #         if i in self.not_letters:
        #             continue
        #         c(nums, target_count, depth + 1, i +
        #           1, current_list + [i], ans)

        # def helper(current_string, remove_count):
        #     if is_valid(current_string):
        #         self.ans.append(current_string)
        #         return True
        #     deleting_indexes_set = []
        #     c([k for k in range(len(current_string))],
        #       remove_count, 0, 0, [], deleting_indexes_set)

        #     result = False
        #     for current_indexes in deleting_indexes_set:
        #         temp_string = ''
        #         for i in range(len(current_string)):
        #             if i not in current_indexes:
        #                 temp_string += current_string[i]
        #         if is_valid(temp_string):
        #             self.ans.append(temp_string)
        #             result = True
        #     return result

        temp_s = ''
        adding_l = False
        # trim ending (
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')':
                adding_l = True
            else:
                if s[i] == '(':
                    if not adding_l:
                        continue
            temp_s = s[i] + temp_s
        s = temp_s

        temp_s = ''
        adding_r = False
        # trim leading )
        for i in range(len(s)):
            if s[i] == '(':
                adding_r = True
            else:
                if s[i] == ')':
                    if not adding_r:
                        continue
            temp_s = temp_s + s[i]
        s = temp_s

        # # calculate the min count of number of char to remove
        # # get indexes of non-letter ele
        # l, r = 0, 0
        # for i in range(len(s)):
        #     if s[i] == '(':
        #         l += 1
        #     elif s[i] == ')':
        #         r += 1
        #     else:
        #         self.not_letters.add(i)
        # current_remove_count = abs(l - r)

        def dfs(current_string: str, start_index, l_count, r_count):
            if l_count == 0 and r_count == 0:
                if is_valid(current_string):
                    self.ans.append(current_string)
                return

            for i in range(start_index, len(current_string)):

                # only pick first ele if there's consecutive identical eles
                if i != start_index and current_string[i - 1] == current_string[i]:
                    continue

                if current_string[i] == '(' or current_string[i] == ')':
                    temp_string = current_string[:i] + current_string[i + 1:]
                    if r_count > 0:
                        dfs(temp_string, i, l_count, r_count - 1)
                    elif l_count > 0:
                        dfs(temp_string, i, l_count - 1, r_count)

        l, r = 0, 0

        for ch in s:
            l += ch == '('
            if l == 0:
                r += ch == ')'
            else:
                l -= ch == ')'
        # print(l, r)

        dfs(s, 0, l, r)
        return self.ans

        # found = False
        # while not found:
        #     found = helper(s, current_remove_count)
        #     current_remove_count += 1

        # return list(set(self.ans))


# @lc code=end
