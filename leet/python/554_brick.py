class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        wallLookupTable = {} # map width of wall to # of the width
        winnerWidthCount = 0
        winnerWidth = 0
        for row in wall:
            wallWidth = 0
            for brickIdx in xrange(len(row) - 1):
                wallWidth += row[brickIdx]
                count = wallLookupTable.get(wallWidth, 0) + 1
                wallLookupTable[wallWidth] = count
                if count > winnerWidthCount:
                    winnerWidthCount = count
                    winnerWidth = wallWidth
        print wallLookupTable
        return len(wall) - winnerWidthCount

if __name__ == '__main__':
    sol = Solution()

    inputWall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
    print sol.leastBricks(inputWall)
