class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Function to return depth of
# the Tree from root
def find_ht(root):
    if (not root):
        return 0

    # If current node is a leaf node
    if (root.left == None and root.right == None):
        return 1

    return max(find_ht(root.left), find_ht(root.right)) + 1


# Function to find the root of the smallest
# subtree consisting of all deepest nodes
def find_node(root):
    global req_node

    if (not root):
        return

    # Stores height of left subtree
    left_ht = find_ht(root.left)

    # Stores height of right subtree
    right_ht = find_ht(root.right)

    # If height of left subtree exceeds
    # that of the right subtree
    if (left_ht > right_ht):

        # Traverse left subtree
        find_node(root.left)

    # If height of right subtree exceeds
    # that of the left subtree
    elif (right_ht > left_ht):
        find_node(root.right)

    # Otherwise
    else:

        # Return current node
        req_node = root
        return


# Driver Code
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(11)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(5)
    root.right.right = TreeNode(10)
    req_node = None
    find_node(root)
    print(req_node.right.val)