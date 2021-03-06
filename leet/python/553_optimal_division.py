class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(num) for num in nums]
        if len(nums) == 1:
           return nums[0]
        elif len(nums) == 2:
           return nums[0] + '/' + nums[1]

        nums[1] = '(' + nums[1]
        nums[len(nums) - 1] += ')'
        return '/'.join(nums)
