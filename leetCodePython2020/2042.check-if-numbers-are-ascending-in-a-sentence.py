#
# @lc app=leetcode id=2042 lang=python3
#
# [2042] Check if Numbers Are Ascending in a Sentence
#

# @lc code=start
class Solution:
    def areNumbersAscending(self, s: str) -> bool:

        prev = -1

        arr = s.split(' ')
        for i in range(len(arr)):
            if arr[i].isnumeric():
                current_number = int(arr[i])
                if current_number > prev:
                    prev = current_number
                else:
                    return False

        return True

# @lc code=end
