# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, lst, root):
        if root == None:
            return
        self.inorder(lst,root.left)
        lst.append(root.val)
        self.inorder(lst,root.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        self.inorder(lst,root)
        return lst