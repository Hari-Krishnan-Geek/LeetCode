# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        result = []
        current = 0
        def findPosition(node):
            print(node.val)
            if node.left:
                findPosition(node.left)

            result.append(node.val)

            if node.right:
                findPosition(node.right)

        findPosition(root)
        return result[k-1]


