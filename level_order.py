from collections import deque

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        ans = []
        depth = 0

        if not root:
            return ans

        q = deque()
        q.append(root)

        while q:
            curr = []
            size = len(q)

        
            for i in range(size):
                
                temp = q.popleft()
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)

                curr.append(temp.val)
            depth = depth + 1
            ans.append(curr)
        return ans,depth
            
    

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(3)
    root.left.left = Node(5)
    root.left.left.left = Node(7)
    root.right = Node(2)
    root.right.right = Node(4)
    root.right.right.right = Node(6)
    
    ob = Solution()

    level,depth = ob.levelOrder(root)
    print("level order travesel ->",level)
    print("Depth of trree->",depth)
