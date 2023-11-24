class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxPathSum(root):
    max_value = [float('-inf')]
    maxPathDown(root, max_value)
    return max_value[0]

def maxPathDown(node, max_value):
    if node is None:
        return 0
    left = max(0, maxPathDown(node.left, max_value))
    right = max(0, maxPathDown(node.right, max_value))
    max_value[0] = max(max_value[0], left + right + node.val)
    return max(left, right) + node.val

if __name__ == "__main__":
    root = Node(-10)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)

    answer = maxPathSum(root)
    print("The Max Path Sum for this tree is", answer)
