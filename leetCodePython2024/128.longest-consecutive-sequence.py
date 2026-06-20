#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_elements = set(nums)
        visited = set()
        prev, count, result = float('-inf'), 0, 0

        def search(current_num, search_left_side, unidirection_length):
            visited.add(current_num)
            if search_left_side:
                next_num = current_num-1
            else:
                next_num = current_num+1

            if next_num in all_elements:
                return search(next_num, search_left_side, unidirection_length+1)
            else:
                return unidirection_length

        for i in all_elements:
            if i not in visited:
                visited.add(i)
                result = max(search(i, True, 0)+search(i, False, 0)+1, result)

        return result


# @lc code=end

def longestConsecutive(self, nums: List[int]) -> int:
        visited = set()
        output = 0
        num_set=set(nums)


        # [60, .... , 59, 58, 57, 56, 55 ..... 61]
        for num in num_set:
          

            if num in visited:
                continue

            prev = num - 1 # 59, 61
            after = num + 1            

            # curr_output = 1
            # while prev in nums:
            while prev in nums_setor prev in visited:
                visited.add(prev)
                prev -= 1
                # curr_output += 1
            # prev = 54
            while after in nums_set:
                visited.add(after)
                after += 1
                # curr_output += 1
            # after = 62
            curr_output after - prev - 1 # 62 - 54
            output = max(output, curr_output)
            

        return output


