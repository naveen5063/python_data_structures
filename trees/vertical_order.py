# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

from collections import deque
import sys
class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
	def verticalOrderTraversal(self, A):
		q = deque()
		level_dict = {}
		#print("level")
		q.append([A, 0])
		minlevel = sys.maxsize
		maxlevel = 1 - sys.maxsize
		while len(q) > 0:
			pair = q[0]
			node = pair[0]
			print("p", pair, node)
			q.popleft()
			level = pair[1]
			print(node.val, level)
			minlevel = min(minlevel, level)
			maxlevel = max(maxlevel, level)
			if level not in level_dict.keys():
				level_dict[level] = [node]
			else:
				level_dict[level] += [node]
			if node.left is not None:
				q.append([node.left, level - 1])
			if node.right is not None:
				q.append([node.right, level + 1])
		print(level_dict)
		print("minlevel", minlevel, maxlevel)
		elelist = []
		for i in range(minlevel, maxlevel+1):
			l1 = []
			temp = level_dict[i]
			for j in range(0, len(temp)):
				l1.append(temp[j].val)
				print(temp[j].val, end="")
			print("\n")
			elelist.append(l1)
		print("l1", elelist)


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
	print(s.verticalOrderTraversal(root))