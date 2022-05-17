from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cache = dict()
        return self.helper(head, 0, cache)
    
    def helper(self, node, pos, cache):
        if not node: return False
        
        if node in cache: 
            return True
            
        cache[node] = pos
        
        return self.helper(node.next, pos+1, cache)