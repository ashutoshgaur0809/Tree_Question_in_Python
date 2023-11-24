class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.result = 0 
        
        def max_depth(root):
            if not root: return 0
            
            left = max_depth(root.left)
            right = max_depth(root.right)
            self.result = max(self.result, left + right)
            return 1+ max(left, right)
            # 1 + max(l + r) kr rahe hai kyu ki ye 0 index se start krega 
    
        max_depth(root)
        return self.result 
        # if not root:
        #     return 0
  