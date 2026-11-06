# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solve(node,minVal,maxVal):
            if node is None:
                return True

            if not(minVal < node.val < maxVal):
                return False

            left = solve(node.left,minVal,node.val)
            right = solve(node.right,node.val,maxVal)

            return left and right
        return solve(root,float('-inf'),float('inf'))
