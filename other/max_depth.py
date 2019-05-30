def maxDepth(self, root):
    """
    Given a binary tree, find its maximum depth.

    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))