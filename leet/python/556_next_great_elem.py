class Solution(object):
    def __list2int(self, nums):
        tot = 0
        for num in nums:
            tot *= 10
            tot += num
        return tot

    def __findHead(self, nums, target):
        minTarget = 10 # more than 0~9
        minTargetIdx = -1
        for i in xrange(len(nums)):
            num = nums[i]
            if num > target and num < minTarget:
                minTarget = num
                minTargetIdx = i
        return minTargetIdx

    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        orgN = n
        lastDigit = -1
        rearrangeDigitArray = []
        nowPos = 0
        while n > 0:
            nowDigit = n % 10
            n = n / 10
            nowPos += 1
            rearrangeDigitArray.append(nowDigit)
            if nowDigit < lastDigit:
                break
            else:
                lastDigit = nowDigit

        if nowDigit >= lastDigit: #incremental array
            return -1
        else:
            headOfTailIdx = self.__findHead(rearrangeDigitArray, nowDigit)
            headOfTail = rearrangeDigitArray.pop(headOfTailIdx)
            rearrangeDigitArray.sort()
            rearrangeDigitArray.insert(0, headOfTail)
            tail = self.__list2int(rearrangeDigitArray)
            ans =  n * (10 ** nowPos) + tail
            if ans > 2147483647:
                return -1
            else:
                return ans


if __name__ == '__main__':
    sol = Solution()
    print -1 == sol.nextGreaterElement(1999999999)
    print 126478 == sol.nextGreaterElement(124876)
    print 12162 == sol.nextGreaterElement(12126)
    print -1 == sol.nextGreaterElement(654321)
    print 612358 == sol.nextGreaterElement(586321)
    print 21 == sol.nextGreaterElement(12)
    print -1 == sol.nextGreaterElement(21)
    print -1 == sol.nextGreaterElement(5)
