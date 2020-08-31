#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start


class Solution:
    def decodeString(self, s: str) -> str:

        def helper(start):
            result = ''
            count = -1
            i = start

            while i < len(s):
                current = ord(s[i])
                # 0-9
                if current in range(48, 58):
                    if count == -1:
                        count = int(s[i])
                    else:
                        count = count * 10
                        count += int(s[i])
                    i += 1
                # [
                elif current == 91:
                    i, sub_result = helper(i + 1)
                    count = count if count != -1 else 1
                    result += count * sub_result
                    count = -1
                # ]
                elif current == 93:
                    return i + 1, result
                elif current in range(97, 123) or current in range(65, 91):
                    result += s[i]
                    i += 1
            return result

        return helper(0)

# @lc code=end
