#
# @lc app=leetcode id=1105 lang=python3
#
# [1105] Filling Bookcase Shelves
#

# @lc code=start
class Solution:
    # def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:

    #     def helper(book_index, remainingWidth, old_layer_height, totoal_height):
    #         if book_index == len(books):
    #             return totoal_height

    #         current_book_width, current_book_height = books[book_index]
    #         current_layer_height = max(current_book_height, old_layer_height)
    #         # book in the same layer
    #         if remainingWidth >= current_book_width:
    #             t1 = helper(book_index+1, remainingWidth-current_book_width,
    #                         current_layer_height, totoal_height-old_layer_height+current_layer_height)
    #         else:
    #             t1 = float('inf')
    #         # book in the new layer
    #         t2 = helper(book_index+1, shelfWidth -
    #                     current_book_width, current_book_height, totoal_height+current_book_height)

    #         return min(t1, t2)

    #     return helper(0, shelfWidth, books[0][1], books[0][1])
    def minHeightShelves(self, books, shelf_width: int) -> int:
        dp = [1000**2+1]*len(books)
        for j in range(len(books)):
            max_h_of_current_layer, current_width = 0, 0

            for i in range(j, -1, -1):

                current_width += books[i][0]

                if current_width > shelf_width:
                    break

                max_h_of_current_layer = max(
                    max_h_of_current_layer, books[i][1])
                dp[j] = min(dp[j], (0 if i == 0 else dp[i-1]) +
                            max_h_of_current_layer)

        return dp[-1]


# @lc code=end
