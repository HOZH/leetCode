#
# @lc app=leetcode id=1108 lang=python3
#
# [1108] Defanging an IP Address
#

# @lc code=start
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return ''.join(list(map(lambda x: x if x != '.' else '[.]', address)))

# @lc code=end
