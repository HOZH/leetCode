

from collections import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        ans = 0
        # bfs
        while len(queue):
            current_layer_size = len(queue)
            while current_layer_size:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                current_layer_size -= 1

            ans += 1

        return ans


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0

        val = self.helper(root, 0)

        return max(val, self.max_depth)

    def _helper(self, root, curr_depth):
        if root is None:
            self.max_depth = max(curr_depth, self.max_depth)
            return
        
        self.helper(root.left, curr_depth + 1)
        self.helper(root.right, curr_depth+ 1)


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p == q == None: # if (p is None and q is not None) or (p is not None and q is None):
            return True

        # if any of p or q is None
        if p is None or q is None:
            return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


# [3,9,20,null,null,15,7]
"""
            3
    9           20
null null     15   7

# lefft, then right
stack = [3, 9, 20, 15, 7]
stack.pop -> 7
.pop -> 15
pop -> 20

breadth first
queue = [3, 9, 20, 15, 7]
queue.pop -> 3
.pop -> 9
-> 20
-> 
"""


stack.pop -> 5
stack.pop -> 4
stack.pop -> 3
...





class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.ans = False

        def helper(node, current_val):
            # Early return if flag is already set to True
            if not node or self.ans is True:
                return
            if node.left is None and node.right is None:
                if node.val+current_val == targetSum:
                    self.ans = True
                    return
            helper(node.left, current_val+node.val)
            helper(node.right, current_val+node.val)

        helper(root, 0)
        return self.ans






122122 -> [1, 122122]
61... -> [2, 61...] # pick left
305.. -> [4, 305..] # left


input = 122122
left = 1, right = 122122, mid = left + (right - left) // 2 = ? 6000
if execute_some_condition():

    right = mid
else:
    left = mid + 1

return left


def execute_some_condition():
    # if mid is the answer, then return true
    # if mid is smaller than the answer, then return false
    # if mid is larger than the answer, then return true


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        candidate = ''
        for i in range(len(s)//2+1):
            candidate+= s[i]
            if len(s) % len(candidate) == 0:

                pass
            else:
                continue
        return False 
    

1,2,3,5,8

current value is sum of previous two values except for first two



what's the sum from 1~10

10*(10-9)/2 = 45

1+2+3+4+5

5*(5-1)//2
5 - 1 = 4 -> 4 * 5 = 20 / 2 = 10



10!
1*2*3*4

n * (n + 1) // 2
x * (x + 1) // 2 = 15
 x*(x+1) = 15 *2
15 *2 = x*(x+1)
30 = x*x + 1*x # 30 = (x + 1/2) ** 2 - 1/4
30 = x+x**2



5 + 1 = 6 -> 6 * 5 = 30 / 2 = 15



1
2 2
3 3 3
4 4 4 4
5 5 5 5 5 




Input: grid = 
[
    [0,1,0,0],
    [1,1,1,1],
    [0,1,0,1],
    [1,1,1,1]
]
Output: 16

index 0 - > row 0
    row 0 -> 0 # ignore
    row 0 -> 1 # found land - > check index 0, index 2
                # if out of boundary or neighbor is 0 -> + 1 edge
    row 1 -> 0




class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        result = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    result += 4
                    # Subtract edges shared with other land cells
                    if r > 0 and grid[r-1][c] == 1:
                        result -= 2
                    if c > 0 and grid[r][c-1] == 1:
                        result -= 2

        return result


Priority is greater than or equal to -> >=
Priority is less than or equal to -> <=
Priority is equal to -> ==

0.0, 0.1, 0.2, 0.3, ... 1.0
1, 2, 3, 4, 5, 6, 7,
enum = {
    1 = "1"
    2 = "2"
    3 = 3
}

> -> >=
=> 0.7 AND <= 0.7
0.7, 0.69 -> 0.7   99999988888887
0.50 -> 0.5 0000000000000000000003
0.5000000000000000002

0.50001


hack_episilon = 0.005
python_epilion = 0.01

equal to 0.7

query > filter.values -> ["7"]
 (value * 0.1) + epislon
 0.500000000000000000000003 + 0.05



5 5 5 20 
10|5 



alex

saeed

alexei -> aaleeexeeii

name   -> typed
aleex -> aaaalexx
        -> xxalee

aleex -> alex

 rick and kric,




((( ))) 
left = 3, r = 0
left = 3, r = 1
left = 3, r = 2
left = 3, r = 3
(( ))

((( ))) ()
left = 3, r = 3
(( )) ()
left = 4, r = 4
(( ))

(()())(())
 ()()  ()

()()
""



1. 
aabba
aaa
''

2. 
aabba
bba
a



azx x zy

azx

xxz -> azzy
azzy
az
azz -> ay



aaa
a
