import bisect

class Solution_N2(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs = sorted(pairs)
        DPList = []
        def fillInDPList(pair):
            longestChainLen = 1
            for length, secondElement in DPList:
                if longestChainLen <= length and secondElement < pair[0]:
                    longestChainLen = length + 1
            DPList.append((longestChainLen, pair[1]))

        for pair in pairs:
            fillInDPList(pair)

        if DPList:
            return max(DPList)[0]
        else:
            return 0

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs = sorted(pairs)
        minSec = 


if __name__ == '__main__':
    sol = Solution()
    print sol.findLongestChain([[1,2], [2,3], [3,4]])
    print sol.findLongestChain([[3,4],[2,3],[1,2]])
    print sol.findLongestChain([])
