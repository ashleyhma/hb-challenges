def isValidBST(self, root, floor = float('-inf'), ceiling = float('inf')):
    """
    Given a binary tree, determine if it is a valid binary search tree (BST).

    Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
    
    :type root: TreeNode
    :rtype: bool
    """
    if root is None:
        return True
    
    if root.val <= floor or root.val >= ceiling:
        return False
    
    return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)