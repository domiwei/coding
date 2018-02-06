# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recursiveFindAns(self, node):
        if node is None:
            return 0, False

        leftSum, leftAns = self.recursiveFindAns(node.left)
        if leftAns == True:
            return 0, True
        rightSum, rightAns = self.recursiveFindAns(node.right)
        if rightAns == True:
            return 0, True

        total = node.val + leftSum + rightSum
        if node.val + leftSum == rightSum and node node.right
        if node.val + min(leftSum, rightSum) == max(leftSum, rightSum):
            return total, True
        return total, False

    def checkEqualTree(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
        _, result = self.recursiveFindAns(root)
        return result
