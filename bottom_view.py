from collections import defaultdict, deque

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class Solution:
    def bottomView(self, root):
        ans = []
        if not root:
            return ans

        # obj creation
        d = defaultdict(int)
        q = deque([(root, 0)])

        while q:
            node, line = q.popleft()
            d[line] = node.val

            if node.left:
                q.append((node.left, line - 1))

            if node.right:
                q.append((node.right, line + 1))

        # sort according to line and take the last value for each line
        for i in sorted(d.keys()):
            ans.append(d[i])

        return ans
    
    def topView(self,root):
        ans = []
        if root == None:
            return 
        d = defaultdict(int)
        q = deque([(root, 0)])

        while q:
            node, line = q.popleft()
            if line not in d:  # Only update if the line is not already in the dictionary
                d[line] = node.val
           

            if node.left:
                q.append((node.left, line - 1))

            if node.right:
                q.append((node.right, line + 1))
            
        for i in sorted(d.keys()):
            ans.append(d[i])

        return ans

# Construct a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.right.left = Node(8)
root.left.right.right = Node(9)

ob = Solution()
bottom_result = ob.bottomView(root)
top_result = ob.topView(root)
print("Bottom View -> ", bottom_result)
print("Top View -> ", top_result)




