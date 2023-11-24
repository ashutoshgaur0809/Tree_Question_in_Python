from collections import defaultdict, deque

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class Solution:
    def verticalOrder(self, root):
        if not root:
            return []

        d = defaultdict(list)
        q = deque([(root, 0)])

        while q:
            node, line = q.popleft()
            # d[line] = node.val isse only bottom view milega aur d = defaultdict(int) use lenge
            d[line].append(node.val)  
            # isse ek line ke correspond sari value d[line] me jaygi aur d = defaultdict(list) use lenge
            # d[-2] = [4]   d[-1] = [2 8] ...
            if node.left:
                q.append((node.left, line - 1))

            if node.right:
                q.append((node.right, line + 1))

        # sort according to line
        result = []
        for i in sorted(d.keys()):
            result.append(d[i])

        return result

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
vertical_order_result = ob.verticalOrder(root)
print("Vertical Order -> ", vertical_order_result)
