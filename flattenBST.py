class Solution:
    def flattenBST(self, root):
        # code here
        import sys
        sys.setrecursionlimit(10**6)
        head=node=Node('*')
        def inorder(root):
            nonlocal node
            if root:
                inorder(root.left)
                node.right=Node(root.data)
                node=node.right
                inorder(root.right)
        inorder(root)
        return head.right

