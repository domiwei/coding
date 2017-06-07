class Solution(object):
    magic = [1, 2, 2]
    __numOfOne = [1, 1, 1]
    __magicSize = 3
    __magicPointer = 2
    __nowSymbol = 1
    def __appendNumber(self, numAppend, symbol):
        for i in xrange(0, numAppend):
            Solution.magic.append(symbol)
            if symbol == 1:
                Solution.__numOfOne.append(Solution.__numOfOne[Solution.__magicSize - 1] + 1)
            else:
                Solution.__numOfOne.append(Solution.__numOfOne[Solution.__magicSize - 1])
            Solution.__magicSize += 1

    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n < Solution.__magicSize:
            return Solution.__numOfOne[n-1]

        while Solution.__magicSize < n:
            self.__appendNumber(Solution.magic[Solution.__magicPointer], Solution.__nowSymbol)
            Solution.__magicPointer += 1 #move

            #Change symbol
            if Solution.__nowSymbol == 1:
                Solution.__nowSymbol = 2
            else:
                Solution.__nowSymbol = 1

        #print Solution.__magicPointer, self.__magicPointer
        return Solution.__numOfOne[n-1]

if __name__ == '__main__':
    sol = Solution()

  #  print 1 == sol.magicalString(1)
  #  print 1 == sol.magicalString(2)
  #  print 1 == sol.magicalString(3)
  #  print 2 == sol.magicalString(4)
    sol = Solution()
    print Solution().magic#, Solution().magicPointer
    print 0 == sol.magicalString(0)
    sol = Solution()
    print 3 == sol.magicalString(6)
    print Solution().magic#, Solution().magicPointer
    sol = Solution()
    print Solution().magic#, Solution().magicPointer
    print 4 == sol.magicalString(8)
    print Solution().magic# , Solution().magicPointer

