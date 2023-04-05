#
# @lc app=leetcode id=2325 lang=python3
#
# [2325] Decode the Message
#

# @lc code=start
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        bag = {}
        temp = list(filter(lambda x: x != ' ', [*key]))

        count = 97
        for i in range(len(temp)):
            if temp[i] not in bag:
                bag[temp[i]] = chr(count)
                count += 1

        ans = ''

        for i in range(len(message)):
            if message[i] != ' ':
                ans += bag[message[i]]
                print(bag[message[i]])
            else:
                ans += ' '

        return ans


# @lc code=end
