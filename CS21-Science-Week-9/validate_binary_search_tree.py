# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.prev = None
    def isValidBST(self,root):
        if root is None:
          return True
        if not self.isValidBST(root.left):
          return False   
        if self.prev is not None and root.val <= self.prev.val:
            return False
        self.prev = root
        return self.isValidBST(root.right)

