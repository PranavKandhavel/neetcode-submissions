class Solution:
    def rightSideView(self,root: Optional[TreeNode]) -> List[int]:
        lst = []

        def dfs(node,level):
            if node is None:
                return

            if level == len(lst):
                lst.append(node.val)

            dfs(node.right,level+1)
            dfs(node.left,level+1)

        dfs(root,0)
        return lst