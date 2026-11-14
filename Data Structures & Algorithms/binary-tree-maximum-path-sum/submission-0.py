# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_maximum = float('-inf')
        summ = 0

        def solve(node):
            nonlocal global_maximum
            nonlocal summ
            node_sum = 0
            if (node is None):
                return 0
            
            left = max(0,solve(node.left))
            right = max(0,solve(node.right))

            node_sum = left + node.val + right
            global_maximum = max(node_sum,global_maximum)

            return node.val + max(left,right)

        solve(root)

        return global_maximum
            