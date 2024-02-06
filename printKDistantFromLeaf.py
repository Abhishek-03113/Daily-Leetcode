def f(root):
            if not root:
                return
            if not root.left and not root.right:
                leaves.append(root)
            f(root.left)
            f(root.right)
        
        d = {}
        q = [root]
        while(q):
            for i in range(len(q)):
                node = q.pop(0)
                if node.left:
                    d[node.left] = node
                    q.append(node.left)
                if node.right:
                    d[node.right] = node
                    q.append(node.right)
    
        leaves = []  # [4,5,8]
        f(root)
    
        while(k):
            for i in range(len(leaves)):
                leaf = leaves.pop(0)
                if leaf in d:
                    leaves.append(d[leaf])
            k -= 1
        return len(set(leaves))
