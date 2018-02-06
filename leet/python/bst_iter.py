from binary_tree_builder import *

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.__stack = []
        self.__now = root
        self.__it = None

    def hasNext(self):
        """
        :rtype: bool
        """
        #print 'aaaaaaa'
        return self.__stack or self.__now

    def next(self):
        if self.__it is None:
            self.__it = self.iterate()
        return next(self.__it)

    def iterate(self):
        """
        :rtype: int
        """
        #print 'aaa'
        #yield 123
        while self.__stack or self.__now:
            #print 'bbb'
            if self.__now:
                #print self.__now.val
                self.__stack.append(self.__now)
                self.__now = self.__now.left
                #print self.__now.val
            else:
                cur = self.__stack.pop()
                self.__now = cur.right
                yield cur.val
        yield None


if __name__ == '__main__':
    tree_root = TreeBuilder.buildTree(range(10))
    print bfsTraverse(tree_root)
    iterator = BSTIterator(tree_root)
    v = []
    #print iterator.next()
    while iterator.hasNext():
    #    print v
        #print iterator.next()
        v.append(iterator.next())
        print '------------------'
    print v
