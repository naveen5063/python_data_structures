class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sorted_array_to_bst(nums):
    print("nums", nums)
    if not nums:
        return None
    mid_val = len(nums) // 2
    print("mid_index", mid_val, "mid val", nums[mid_val])
    node = TreeNode(nums[mid_val])
    print("node left")
    node.left = sorted_array_to_bst(nums[:mid_val])
    print("node right")
    node.right = sorted_array_to_bst(nums[mid_val + 1:])
    #print("node val", node.val)
    return node


def preOrder(node):
    if not node:
        return

    #print(node.val)
    preOrder(node.left)
    print(node.val)
    preOrder(node.right)


A = [5,1,4,3,6]
#A.sort()
result = sorted_array_to_bst(A)
#result = sorted_array_to_bst([1, 2, 3, 4, 5, 6, 7])
#result = sorted_array_to_bst([1, 2, 3, 4, 5, 6, 6, 6, 6])
preOrder(result)