# Soluton found in discussion
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        # @param {TreeNode} root
        # @return {integer}
        def countNodes(self, root):
            if not root:
                return 0
            leftDepth = self.getDepth(root.left)
            rightDepth = self.getDepth(root.right)
            if leftDepth == rightDepth:
                return pow(2, leftDepth) + self.countNodes(root.right)
            else:
                return pow(2, rightDepth) + self.countNodes(root.left)
    
        def getDepth(self, root):
            if not root:
                return 0
            return 1 + self.getDepth(root.left)
