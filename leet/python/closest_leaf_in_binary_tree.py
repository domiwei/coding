from binary_tree_builder import *

class Solution:
    def findClosestLeaf(self, root, key):
        def findKeyNode(node):
            if node is None:
                return None
            if node.val == key:
                return node
            left_search = findKeyNode(node.left)
            if left_search is not None:
                return left_search
            return findKeyNode(node.right)

        def isLeaf(node):
            return node.left is None and node.right is None

        node = findKeyNode(root)
        queue = [node]
        dis = 0
        finish = False
        while not finish and queue != []:
            length = len(queue)
            for i in xrange(len(queue)):
                if isLeaf(queue[i]):
                    finish = True
                    break
                if queue[i].left:
                    queue.append(queue[i].left)
                if queue[i].right:
                    queue.append(queue[i].right)
            queue = queue[length:]
            if not finish:
                dis += 1
        return dis

if __name__ == '__main__':
    node_val = ['a',
            'b', 'c', 
            None, None, 'e', 'f',
            None, None, None, None, 'g', None, None, 'h',
            None, None, None, None, None, None, None, None, 'i', 'j', None, None, None, None, 'k', None]
    tree_root = TreeBuilder.buildTree(node_val)
    print bfsTraverse(tree_root)
    sol = Solution()
    print sol.findClosestLeaf(tree_root, 'h'), 1
    print sol.findClosestLeaf(tree_root, 'c'), 2
    print sol.findClosestLeaf(tree_root, 'b'), 0
