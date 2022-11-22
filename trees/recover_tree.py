# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def recoverTree(self, A):
		inorder_arr = []
		swap_nodes = []
		self.inorder(A, inorder_arr)
		for i in range(0, len(inorder_arr)):
			if inorder_arr[i] > inorder_arr[i + 1]:
				swap_nodes.append(inorder_arr[i])
				break
		for i in range(len(inorder_arr)-1, -1, -1):
			if inorder_arr[i] < inorder_arr[i - 1]:
				swap_nodes.append(inorder_arr[i])
				break
		return swap_nodes

	def inorder(self, A, inorder_arr):
		if A is None:
			return
		self.inorder(A.left, inorder_arr)
		inorder_arr.append(A.val)
		self.inorder(A.right, inorder_arr)


if __name__ == '__main__':
	root = TreeNode(5)
	root.left = TreeNode(7)
	root.right = TreeNode(8)
	root.right.right = TreeNode(10)
	root.left.left = TreeNode(3)
	root.left.right = TreeNode(6)
	s = Solution()
	print(s.recoverTree(root))