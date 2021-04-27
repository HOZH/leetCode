#
# @lc app=leetcode id=535 lang=python3
#
# [535] Encode and Decode TinyURL
#

# @lc code=start
class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

        return longUrl[::-1]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return shortUrl[::-1]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end
