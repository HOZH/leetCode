#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        digits = list(map(lambda x: int(x), [*str(num)]))[::-1]
        letters_by_rank = {
            1: {1: 'I', 4: 'IV', 5: 'V', 9: 'IX'},
            2: {1: 'X', 4: 'XL', 5: 'L', 9: 'XC'},
            3: {1: 'C', 4: 'CD', 5: 'D', 9: 'CM'},
            4: {1: 'M'}
        }
        rank = 1
        for i in digits:
            if i == 0:
                rank += 1
                continue

            candinates_dict = letters_by_rank[rank]
            reverse_sorted_candinates_keys = sorted(
                candinates_dict.keys(), reverse=True)
            key_index = 0

            local_result = ''
            while i != 0:
                current_candinator = reverse_sorted_candinates_keys[key_index]
                if i == current_candinator:
                    local_result = local_result + \
                        candinates_dict[current_candinator]
                    i = 0
                    key_index += 1
                elif i > current_candinator:
                    i = i - current_candinator
                    local_result = local_result + \
                        candinates_dict[current_candinator]
                # else:
                elif i < current_candinator:
                    key_index += 1

            result = local_result + result
            rank += 1

        return result

# @lc code=end
