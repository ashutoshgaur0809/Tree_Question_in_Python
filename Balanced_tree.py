class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Node) -> bool:
        return self.dfs_height(root) != -1   #self.dfs_height(root) -> -1 toh -1 != -1 -> False
                                              #self.dfs_height(root) -> not -1 toh not(-1) != -1 True
                                            

    def dfs_height(self, root:Node) -> int:
        if not root:
            return 0

        left_height = self.dfs_height(root.left)
        if left_height == -1:
            return -1

        right_height = self.dfs_height(root.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(3)
    root.left.left = Node(5)
    root.left.left.left = Node(7)
    root.right = Node(2)
    root.right.right = Node(4)
    root.right.right.right = Node(6)
    
    ob = Solution()

    check = ob.isBalanced(root)
    print(check)