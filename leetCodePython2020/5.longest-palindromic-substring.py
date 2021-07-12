#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start


class Solution:

    def longestPalindrome(self, s: str) -> str:
        self.ans = ''

        def helper(l, r):

            if 0 <= l and r < len(s) and s[l] == s[r]:
                farther = helper(l-1, r+1)
                return farther
            else:
                return l+1, r-1

            # while 0 <= l and r < len(s) and s[l] == s[r]:
            #     self.ans = max(self.ans, s[l:r+1], key=len)
            #     l, r = l-1, r+1

        for i in range(len(s)):

            # odd
            # odd = helper(i, i)
            odd_l, odd_r = helper(i, i)
            odd_result = s[odd_l:odd_r+1]

            # even
            # even = helper(i, i+1)
            even_l, even_r = helper(i, i+1)
            even_result = s[even_l:even_r+1] if even_l != even_r else ''

            self.ans = max(self.ans, odd_result, even_result, key=len)
        return self.ans

    def longestPalindrome_slow(self, s: str) -> str:

        s_len = len(s)
        # valid = set()
        valid = set(s)
        valid.add('')

        if len(s) < 2:
            return s

        def helper(current):
            if current in valid:
                return True
            if current[0] == current[-1]:
                temp = helper(current[1:-1])
                if temp:
                    valid.add(temp)
                    return True
                else:
                    return False
            else:
                return False

        for length in range(s_len, 0, -1):

            for i in range(s_len-length+1):

                if helper(s[i:i+length]):
                    return s[i:i+length]

    def longestPalindrome_temp(self, s: str) -> str:

        def helper(current, l, r):
            while l >= 0 and r < len(current) and current[l] == current[r]:
                l, r = l-1, r+1
            return s[l+1:r]

        res = ''
        for i in range(len(s)):

            # odd case
            odd = helper(s, i, i)
            # even case
            even = helper(s, i, i+1)

            res = max(res, even, odd, key=len)

        return res


# @lc code=end
