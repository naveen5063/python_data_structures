
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def possibleBST(root):
    if root is None:
        return 0

def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)

class Solution:
    def generateTrees(self, n: int):

        def dfs(m, n):
            if m == n:
                return [TreeNode(m)]
            if m > n:
                return [None]

            res = []
            # take each value as root node
            for node in range(m, n + 1):
                for left in dfs(m, node - 1):
                    # iterate all root node till right sub tree
                    for right in dfs(node + 1, n):
                        treeNode = TreeNode(node)
                        treeNode.left = left
                        treeNode.right = right
                        inOrder(treeNode)
                        res.append(treeNode)

            return res

        return dfs(1, n)

u = Solution()
print(u.generateTrees(2))