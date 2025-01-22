#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#

# @lc code=start
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # ans = []
        # products.sort()
        # for i in range(len(searchWord)):
        #     local_ans = []
        #     prefix = searchWord[:i+1]
        #     liz = list(filter(lambda x: x.startswith(prefix), products))
        #     count = 0
        #     for i in liz:
        #         if (count) == 3:
        #             break
        #         local_ans.append(i)
        #         count += 1
        #     ans.append(local_ans)

        # return ans
    
        class TrieNode:
            def __init__(self):
                self.children = collections.defaultdict(TrieNode)
                self.suggestion = []

            def add_sugestion(self, product):
                if len(self.suggestion) < 3:
                    self.suggestion.append(product)

        products = sorted(products)
        root = TrieNode()
        for p in products:
            node = root
            for char in p:
                node = node.children[char]
                node.add_sugestion(p)

        result, node = [], root
        for char in searchWord:
            node = node.children[char]
            result.append(node.suggestion)
        return result

# @lc code=end
