class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        def computeSmooth(M, row, col):
            count = 0
            sumSmooth = 0
            for i in xrange(row - 1, row + 2):
                for j in xrange(col - 1, col + 2):
                    if i < 0 or j < 0 or i >= len(M) or j >= len(M[0]):
                        continue
                    sumSmooth += M[i][j]
                    count += 1
            return sumSmooth / count
            
        smooth = []
        for i in xrange(len(M)):
            smooth.append([])
            for j in xrange(len(M[0])):
                smooth[i].append(computeSmooth(M, i, j))
        return smooth

class Solution2(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        def basicComputeSmooth(M, row, col):
            count = 0
            sumSmooth = 0
            for i in xrange(row - 1, row + 2):
                for j in xrange(col - 1, col + 2):
                    if i < 0 or j < 0 or i >= len(M) or j >= len(M[0]):
                        continue
                    sumSmooth += M[i][j]
                    count += 1
            return sumSmooth, count

        def computeSmooth(M, row, col, sumSmooth, count):
            for i in xrange(row - 1, row + 2):
                j = col + 1
                if i >= 0 and j >= 0 and i < len(M) and j < len(M[0]):
                    sumSmooth += M[i][j]
                    count += 1
                j = col - 2
                if i >= 0 and j >= 0 and i < len(M) and j < len(M[0]):
                    sumSmooth -= M[i][j]
                    count -= 1
            return sumSmooth, count
            
        smooth = []
        for i in xrange(len(M)):
            smooth.append([])
            nowSum = 0
            for j in xrange(len(M[0])):
                if j == 0:
                    nowSum, nowCount = basicComputeSmooth(M, i, j)
                else:
                    nowSum, nowCount = computeSmooth(M, i, j, nowSum, nowCount)
                smooth[i].append(nowSum/nowCount)
        return smooth

def main():
    sol = Solution2()
    print [[0,0,0],[0,0,0],[0,0,0]] == sol.imageSmoother([[1,1,1],
        [1,0,1],
        [1,1,1]])

    print [[33,22,22,32],[29,40,39,51],[28,39,34,43],[12,38,50,64]] == sol.imageSmoother([[6,2,5,123],[123,1,0,1],[1,46,177,1], [1,0,4,77]])
    print [[55]] == sol.imageSmoother([[55]])

main()
