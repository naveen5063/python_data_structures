# Python3 program to construct binary
# tree from given array in level
# order fashion Tree Node

# Helper function that allocates a
# new node
import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getNode(data):

    # Allocate memory
    newNode = Node(data)

    # put in the data
    newNode.data = data
    newNode.left = None
    newNode.right = None
    return newNode

def insert_level_order(root, data):
    if (root == None):
        print("root none ", root)
        root = getNode(data)
        print("root none data", root.data)
        return root

    if (data <= root.data):
        print("root left data", root.left, data)
        root.left = insert_level_order(root.left, data)
        print("root left returned", root.left.data)
    else:
        print("root right data", root.right, data)
        root.right = insert_level_order(root.right, data)
        print("root right returned", root.right.data)
    return root

def constructBst(arr, n):
    minSize = -sys.maxsize - 1
    if (n == 0):
        return None
    root = None

    for i in range(0, n):
        if arr[i] is not None:
            print("root dat", arr[i])
            root = insert_level_order(root, arr[i])
            print("root returned", root.data, arr[i])

    return root

def inOrder(root):
    if (root == None):
        return None

    print(root.data, end=" ")
    inOrder(root.left)

    inOrder(root.right)


# Driver Code
if __name__ == '__main__':
    arr = [7, 4, 12, 3, 6, 8, 1, 5, 10]
    #arr = [2, 1, 3]
    arr = [5, 1, 4, 3, 6]
    n = len(arr)
    root = constructBst(arr, n)
    print("left", root.left.data)
    #bst = Constuct_bst()
    #root = bst.constructBst(arr, n)
    #print("", inOrder(root))
    print("Inorder Traversal: ", end="")
    inOrder(root)
