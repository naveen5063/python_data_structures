class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    # def floorTree(self, A):
    #     temp = A.left
    #     while temp.right is not None:
    #         temp = temp.right
    #     return temp.val
    #
    # def ceilTree(self, A):
    #     temp = A.right
    #     while temp.left is not None:
    #         temp = temp.left
    #     return temp.val

    def solve(self, A, B):
        res = []
        for val in B:
            ans = self.get_floor_ceil(A, -1, -1, val)
            print("ans", ans)
            res.append(ans)
        print("res", res)
    def get_floor_ceil(self, root, floor, ceil, key):
        #print("floor, ceil", floor, ceil)
        # base case
        if root is None:
            return [floor, ceil]

        # if a node with the desired value is found, both floor and ceil is equal
        # to the current node
        if root.val == key:
            #print("equal")
            return [root.val, root.val]

        # if the given key is less than the root node, recur for the left subtree
        elif key < root.val:
            # update ceil to the current node before visiting the left subtree

            return self.get_floor_ceil(root.left, floor, root.val, key)

        # if the given key is more than the root node, recur for the right subtree
        else:
            # update floor to the current node before visiting the right subtree
            return self.get_floor_ceil(root.right, root.val, ceil, key)


if __name__ == '__main__':
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.right.left = TreeNode(10)
    # root.right.left.left = TreeNode(9)
    # root.left.right = TreeNode(4)
    # root.left.right.right = TreeNode(5)
    root = TreeNode(10)
    root.left = TreeNode(4)
    root.right = TreeNode(15)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(8)

    s = Solution()
    B = [4, 19]
    s.solve(root, B)
