from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        return self.helper(root, targetSum, 0)

    def helper(self, root, target, total_sum):
        if not root:
            return False

        total_sum += root.val

        if self.is_leaf(root):
            return target == total_sum

        left = self.helper(root.left, target, total_sum)
        right = self.helper(root.right, target, total_sum)

        return left or right

    def is_leaf(self, root):
        return not root.left and not root.right
