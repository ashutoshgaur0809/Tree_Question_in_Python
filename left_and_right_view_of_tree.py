from collections import deque, defaultdict
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root, level=0, r_list=None):
        if r_list is None:
            r_list = []

        if root is None:
            return r_list

        if len(r_list) == level:
            r_list.append(root.val)

        self.rightSideView(root.right, level + 1, r_list)
        self.rightSideView(root.left, level + 1, r_list)

        return r_list
    
    def leftSideView(self, root, level=0, l_list=None):
        if l_list is None:
            l_list = []

        if root is None:
            return l_list

        if len(l_list) == level:
            l_list.append(root.val)

        self.leftSideView(root.left, level + 1, l_list)
        self.leftSideView(root.right, level + 1, l_list)

        return l_list
    
   

                

# Example usage:
# Construct a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.left = TreeNode(4)
root.left.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Create an instance of the Solution class
ob = Solution()
r_list = []
right_result = ob.rightSideView(root,0,r_list)
l_list = []

left_result = ob.leftSideView(root,0,l_list)



# Print the result
print("Right Side View:", right_result)
print("Left Side View:", left_result)

