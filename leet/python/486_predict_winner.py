class Solution():
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numLen = len(nums)
        dpTable = [[0 for x in range(numLen)] for y in range(numLen)]
        bestChoiceIsStartTable = [[True for x in range(numLen)] for y in range(numLen)]
        def fetchDPvalue(start, end):
            if start < 0 or start >= numLen or end < 0 or end >= numLen:
                return 0
            else:
                return dpTable[start][end]

        def isBestChoiceStart(start, end):
            if start < 0 or start >= numLen or end < 0 or end >= numLen:
                return True
            else:
                return bestChoiceIsStartTable[start][end]
                #if start + 1 >= numLen:
                #    return True
                #if dpTable[start][end] == nums[start] + dpTable[start + 1][end]:
                #    return True
                #else:
                #    return False

        for index in xrange(numLen):
            for shift in xrange(numLen - index):
                start = shift
                end = index + shift
                # case choose start index:
                if isBestChoiceStart(start + 1, end):
                    startValue = nums[start] + fetchDPvalue(start + 2, end)
                else:
                    startValue = nums[start] + fetchDPvalue(start + 1, end - 1)

                if isBestChoiceStart(start, end - 1):
                    endValue = fetchDPvalue(start + 1, end - 1) + nums[end]
                else:
                    endValue = fetchDPvalue(start, end - 2) + nums[end]

                # fill dp table
                if startValue > endValue:
                    dpTable[start][end] = startValue
                    bestChoiceIsStartTable[start][end] = True
                else:
                    dpTable[start][end] = endValue
                    bestChoiceIsStartTable[start][end] = False

        print dpTable
        if dpTable[0][numLen-1] * 2 >= sum(nums):
            return True
        else:
            return False

sol = Solution()
print False == sol.PredictTheWinner([1, 3, 1])
print False == sol.PredictTheWinner([1, 5, 2])
print True == sol.PredictTheWinner([1, 5, 233, 7])
