class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            if p.val == q.val:  #preorder dona ka sath m ,,,,ek ka l dusure ka l ek ka r dusre ka r
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False