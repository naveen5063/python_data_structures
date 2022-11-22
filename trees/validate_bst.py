import sys


class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to insert nodes in level order
def insertLevelOrder(arr, root, i, n):
    # Base case for recursion
    print("i", i)
    if i < n:
        temp = newNode(arr[i])
        root = temp

        # insert left child
        root.left = insertLevelOrder(arr, root.left,
                                     2 * i + 1, n)

        # insert right child
        root.right = insertLevelOrder(arr, root.right,
                                      2 * i + 2, n)
    return root


# Function to print tree nodes in
# InOrder fashion
def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)


def isBST(root, l=None, r=None):
    # Base condition
    if root is None:
        return True

    if l is not None and root.data <= l.data:
        return False

    if r is not None and root.data >= r.data:
        return False

    # check recursively for every node.
    #print(root.left.data, l.data, root.data)
    return isBST(root.left, l, root) and \
           isBST(root.right, root, r)


minval = 1 - sys.maxsize
maxval = sys.maxsize


def isValidBst(root):
    return checkBst(root, minval, maxval)


def checkBst(root, minval, maxval):
    if root is None:
        return True
    if root.data >= maxval or root.data <= minval:
        return False
    return checkBst(root.left, minval, root.data) and checkBst(root.right, root.data, maxval)


# Driver Code
if __name__ == '__main__':
    root = newNode(3)
    root.left = newNode(2)
    root.right = newNode(5)
    root.right.left = newNode(4)
    root.right.right = newNode(6)

    # root = newNode(4)
    # root.left = newNode(2)
    # root.right = newNode(5)
    # root.left.left = newNode(1)
    # root.left.right = newNode(3)
    # root.right.left.left = newNode(40)

    A = [4, 2, 5, 1, 3]
    # A = [3, 2 , 5, 4, 6]
    n = len(A)
    root = None
    root = insertLevelOrder(A, root, 0, n)
    #print("inOrder", inOrder(root))
    #if (isBST(root, None, None)):
    if isValidBst(root):
        print("Is BST")
    else:
        print("Not a BST")
