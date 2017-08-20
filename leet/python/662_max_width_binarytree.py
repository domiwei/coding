# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue
class TreeNodeMore(object):
    def __init__(self, node, pos):
        self.node = node
        self.pos = pos

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        q = Queue.Queue()
        q.put(TreeNodeMore(root, 0))
        maxWidth = 0

        while q.empty() is False :
            qsize = q.qsize()
            levelWidth = []
            for _ in xrange(qsize):
                tnode = q.get()
                pos = tnode.pos
                levelWidth.append(pos)
                if tnode.node.left:
                    q.put(TreeNodeMore(tnode.node.left, pos * 2))
                if tnode.node.right:
                    q.put(TreeNodeMore(tnode.node.right, pos * 2 + 1))
            left = min(levelWidth)
            right = max(levelWidth)
            width = right - left + 1
            maxWidth = max(width, maxWidth)
        return maxWidth
