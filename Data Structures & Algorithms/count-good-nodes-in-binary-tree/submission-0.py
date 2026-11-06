# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def calc(node,maxVal):
            nonlocal count

            if node is None:
                return
            if node.val >= maxVal:
                count += 1
                maxVal = node.val

            calc(node.left,maxVal)
            calc(node.right,maxVal)
            return count

        ans = calc(root,root.val)
        return ans





