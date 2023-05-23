"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        # BFS method
        if root == None:
            return None

        q = [root]
        
        while q:
            limit = len(q)

            while(limit):

                node = q.pop(0)
                if limit > 1:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                    q.append(node.right)

                limit -= 1

        return root

            




            
