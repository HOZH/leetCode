#
# @lc app=leetcode id=821 lang=python3
#
# [821] Shortest Distance to a Character
#

# @lc code=start
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        length = len(s)
        result = [float('inf')]*len(s)

        def update_list(original_index):
            result[original_index] = 0
            count = 0
            for i in range(original_index+1, length):
                count += 1
                if result[i] > count:
                    result[i] = count
                else:
                    break
            count = 0
            for i in range(original_index-1, -1, -1):
                count += 1
                if result[i] > count:
                    result[i] = count
                else:
                    break

        for i in range(len(s)):
            if s[i] == c:
                update_list(i)

        return result


# @lc code=end

# s=az c='a' -> [0, 1]
# s = "aaazabz", c = "z" -> [3,2,1,0]
# [0,25] or [0,1]
Input: s = "lov el eetcode", c = "e"
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        output = [float('inf') for char in s]
        indices = []

        for i, char in enumerate(s):
            if char == c:
                indices.append(i)

        j = 1
        for i, char in enumerate(s):
            prev_mapped_index = indices[j-1]
            next_mapped_index = indices[j - 1]
            if j < len(indices):
                next_mapped_index = indices[j]
            diff = min(abs(prev_mapped_index - i), abs(next_mapped_index - i))
            output[i] = diff
            if j < len(indices) and i == indices[j]:
                j += 1

        return output
    

s = abbbccc a c=a
    0123321 0

0123456*


___*3210

s = ababababab c = a


