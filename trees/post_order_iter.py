class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def postorderTraversal(self, A):
		stack1 = []
		stack2 = []
		stack1.append(A)
		while len(stack1) > 0:
			temp = stack1.pop()
			print("temp", temp.val)
			stack2.append(temp.val)
			if temp.left:
				stack1.append(temp.left)
			if temp.right:
				stack1.append(temp.right)
			print("stack2", stack2)
		stack2.reverse()
		return stack2




if __name__ == '__main__':
	# root = TreeNode(1)
	# root.left = TreeNode(6)
	# root.right = TreeNode(2)
	# root.right.left = TreeNode(3)
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.right.left = TreeNode(4)
	root.right.left.right = TreeNode(5)
	s = Solution()
	print(s.postorderTraversal(root))