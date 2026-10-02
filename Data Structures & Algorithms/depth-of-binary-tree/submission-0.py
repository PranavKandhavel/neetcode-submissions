class Solution:
    def maxDepth(self,root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        count = max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1

        return count