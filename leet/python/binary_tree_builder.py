class Node(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# 0,1,2,3,4,5,6
#left: 1, 3, 4, 7,8,9,10
class TreeBuilder(object):
    @staticmethod
    def recBuildTree(node_list, index):
        if index >= len(node_list):
            return None
        if node_list[index] is None:
            return None

        now = Node(node_list[index])
        now.left = TreeBuilder.recBuildTree(node_list, index*2+1)
        now.right = TreeBuilder.recBuildTree(node_list, index*2+2)
        return now

    @staticmethod
    def buildTree(node_list):
        def checkValid():
            valid = True
            for i in xrange(1, len(node_list)):
                if node_list[i] is not None:
                    parent_index = (i-1)/2
                    if node_list[parent_index] is None:
                        valid = False
                        break
            return valid
        
        if not checkValid():
            return None

        return TreeBuilder.recBuildTree(node_list, 0)


def bfsTraverse(root):
    if root is None:
        return []

    now = root
    queue = [root]
    ans = []
    while queue != []:
        length = len(queue)
        for i in xrange(length):
            ans.append(queue[i].val)
            if queue[i].left:
                queue.append(queue[i].left)
            if queue[i].right:
                queue.append(queue[i].right)
        queue = queue[length:]
    return ans


if __name__ == '__main__':
    node_val = range(100)
    tree_root = TreeBuilder.buildTree(node_val)
    print bfsTraverse(tree_root)
    print bfsTraverse(TreeBuilder.buildTree([]))
    print bfsTraverse(TreeBuilder.buildTree([5]))
    print bfsTraverse(TreeBuilder.buildTree([5,6,None,8,9,10,11]))
