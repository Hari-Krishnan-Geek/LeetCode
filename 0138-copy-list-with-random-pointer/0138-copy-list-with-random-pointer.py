"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        result = {}

        node = head
        if not node:
            return None
        
        while node:
            result[node] = Node(node.val)
            node = node.next

        for key in result.keys():
            result[key].next = None if not key.next else result[key.next]
            result[key].random = None if not key.random else result[key.random]

        return result[head]
