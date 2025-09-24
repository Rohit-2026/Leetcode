# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a=[]
        def ino(root):
            if root==None:
                return a
            ino(root.left)
            a.append(root.val)
            ino(root.right)
        ino(root)    
        return a
        