#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#

# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        uni = set()

        for i in emails:

            local, domain = i.split('@')

            local = local.replace('.', '')

            isPlusSign = local.find('+')

            if isPlusSign != -1:

                local = local[:isPlusSign]

            uni.add(local+'@'+domain)

        return len(uni)


# @lc code=end
