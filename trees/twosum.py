# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, A, B):
        inorder_arr = []
        self.get_inorder(A, inorder_arr)
        i = 0
        j = len(inorder_arr)-1

        while(i < j):
            twosum = inorder_arr[i] + inorder_arr[j]
            if twosum == B:
                return 1
            elif twosum > B:
                j -= 1
            else:
                i += 1
        return 0

    def get_inorder(self, A, inorder_arr):
        if A is None:
            return
        self.get_inorder(A.left, inorder_arr)
        inorder_arr.append(A.val)
        self.get_inorder(A.right, inorder_arr)