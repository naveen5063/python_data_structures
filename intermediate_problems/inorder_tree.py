class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        inorder_arr = []

        self.inorderTraversalUtil(A, inorder_arr)
        return inorder_arr

    def inorderTraversalUtil(self, A, inorder_arr):

        if A is None:
            return

        self.inorderTraversalUtil(A.left, inorder_arr)
        inorder_arr.append(A.val)
        self.inorderTraversalUtil(A.right, inorder_arr)
        return


A = {1 2 3 -1 -1 4 -1 -1 5 -1 -1}
