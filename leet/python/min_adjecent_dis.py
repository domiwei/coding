import functools

class Solution(object):
    def find_min_adjecent_dis(self,nums):

        def cmp_ftn(item1, item2):
            if item1[0] != item2[0]:
                #print item1[0], item2[0]
                return item1[0] > item2[0]
            else:
                return item1[1] > item2[1]
                

        sorted_nums = []
        for i, num in enumerate(nums):
            sorted_nums.append((num, i))
        #sorted(sorted_nums, key=functools.cmp_to_key(cmp_ftn))
        sorted_nums = sorted(sorted_nums, key=lambda x: (x[0], x[1]))
        min_dis = -2
        for i, this_tuple in enumerate(sorted_nums):
            pass

            


#sol = Solution()
#sol.find_min_adjecent_dis([1,2,8,4,9,2,3,3,3,7])



def xxx(nums):
    nums.sort()
    min_dis = -2
    for i in xrange(len(nums)-1):
        min_dis = min(min_dis, abs(nums[i]-nums[i+1]))
    if min_dis > 1000000:
        return -1
    elif min_dis > 0:
        return min_dis
    else:
        return -2

def num_castle(nums):
    prev_num = None
    count = 0
    for i in xrange(len(nums)-1):
        if nums[i] > nums[i+1]:
            if not prev_num or prev_num < nums[i]:
                print nums[i]
                count += 1
            prev_num = nums[i]
        elif nums[i] < nums[i+1]:
            if not prev_num or prev_num > nums[i]:
                print nums[i]
                count += 1
            prev_num = nums[i]
    return count + 1

print num_castle([2,2,3,4,3,3,2,2,1,1,2,5])
