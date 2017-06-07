class Solution(object):
    def recursiveFind(self, nowNode, depth):
        if self._maxDepth < depth:
            self._maxDepth = depth
            self._maxLeftDepthValue = nowNode.val

        if nowNode.left != None:
            self.recursiveFind(nowNode.left, depth + 1)
        if nowNode.right != None:
            self.recursiveFind(nowNode.right, depth + 1)

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self._maxDepth = 0
        self._maxLeftDepthValue = root.val
        self.recursiveFind(root, 0)
        return self._maxLeftDepthValue
