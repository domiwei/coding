class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absentCount = 0
        continuousLate = 0
        rewards = True
        prevChar = 'N'
        for i in xrange(len(s)):
            nowChar = s[i]
            if nowChar == 'A':
                continuousLate = 0
                absentCount += 1
                if absentCount > 1:
                    rewards = False
                    break
            elif nowChar == 'L':
                if prevChar == 'L':
                    continuousLate += 1
                    if continuousLate > 1:
                        rewards = False
                        break
            else:
                continuousLate = 0
            prevChar = nowChar

        return rewards

class Solution2(object):
    def checkRecord(self, s):
        return s.count('A') <= 1 and 'LLL' not in s

if __name__ == '__main__':
    sol = Solution()

    print True == sol.checkRecord('PPALLP')
    print True == sol.checkRecord('P')
    print True == sol.checkRecord('A')
    print True == sol.checkRecord('L')
    print True == sol.checkRecord('LL')
    print True == sol.checkRecord('PPAP')
    print True == sol.checkRecord('PPAPL')
    print True == sol.checkRecord('LPPAPL')
    print False == sol.checkRecord('PPALLLP')
    print False == sol.checkRecord('LLL')
    print False == sol.checkRecord('PAA')
    print False == sol.checkRecord('AA')
