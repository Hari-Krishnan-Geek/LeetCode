# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:


        # each call to this helper function will add the list ofnode values of a level to result
        def helper(result, q):

            # "q" holds nodes in the current level.
            size = len(q)

            # 'current'  will hold the values of nodes in the current level
            current = []

            # read all the nodes in the current level
            while size:
                node = q.pop(0)
                current.append(node.val)

                # add the child nodes into q to get considered for next helper() function call, i,e for next level iteration
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                size -= 1 
            result.append(current)

            # if there is no new value added for next level return result, else call helper()for next level
            if q:
                helper(result, q)
            else:
                return result

        if root:
            q = [root]

            result = []
            helper(result, q)

            return result
        else:
            return []



