class Solution:
    def kthSmallest(self,root: Optional[TreeNode],k: int) -> int:
        cnt = k

        def solve(node):
            nonlocal cnt

            if node is None:
                return

            left = solve(node.left)

            if left is not None:
                return left

            cnt -= 1

            if cnt == 0:
                return node.val

            right = solve(node.right)

            if right is not None:
                return right

        return solve(root)