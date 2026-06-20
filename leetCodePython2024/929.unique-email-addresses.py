#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#

# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        normalized_emails = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = local_name.split('+', 1)[0].replace('.', '')
            normalized_emails.add(f'{local_name}@{domain_name}')

        return len(normalized_emails)
        email_set = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = local_name.split('+')[0]
            # local_name = ''.join(list(filter(lambda x: x != '.', local_name)))
            local_name = local_name.replace('.', '')
            email_set.add(local_name+'@'+domain_name)
        return len(email_set)

# @lc code=end
