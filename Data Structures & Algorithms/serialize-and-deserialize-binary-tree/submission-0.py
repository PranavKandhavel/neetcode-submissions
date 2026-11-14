
class Codec:

    def serialize(self,root):
        if not root:
            return ""

        result = []
        q = [root]
        i = 0

        while i < len(q):
            node = q[i]
            i += 1

            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append("N")

        return ",".join(result)


    def deserialize(self,data):
        if not data:
            return None

        values = data.split(",")

        root = TreeNode(int(values[0]))
        q = [root]
        i = 1
        j = 0

        while j < len(q):
            node = q[j]
            j += 1

            if values[i] != "N":
                node.left = TreeNode(int(values[i]))
                q.append(node.left)
            i += 1

            if values[i] != "N":
                node.right = TreeNode(int(values[i]))
                q.append(node.right)
            i += 1

        return root
