from ast import List
from collections import defaultdict
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)
        self.helper(root, levels, currentLevel=1)
        solution = []
        
        for key in sorted(levels.keys()):
            solution.append(levels[key])
        
        return solution
    
    def helper(self, root, levels, currentLevel):
        if not root:
            return
        
        levels[currentLevel].append(root.val)
        
        self.helper(root.left, levels, currentLevel+1)  # Left side
        self.helper(root.right, levels, currentLevel+1)  # Right side        