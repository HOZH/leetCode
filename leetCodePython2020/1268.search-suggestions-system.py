#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#

# @lc code=start


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        products.sort()

        result = []
        current_word = ''

        for i in range(len(searchWord)):

            current_word += searchWord[i]

            products = list(
                filter(lambda x: x.startswith(current_word), products))
            result.append(products[:3])

        return result


# @lc code=end
