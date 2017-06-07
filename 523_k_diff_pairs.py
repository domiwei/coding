class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        len_nums = len(nums)

        pair_count = 0
        target_idx = 1
        last_pair = (0, -1)
        for idx in xrange(0, len_nums):
            target_idx = max(target_idx, idx + 1)

            while target_idx < len_nums:
                dis = nums[target_idx] - nums[idx]
                if dis < k:
                    target_idx += 1
                    continue
                elif dis == k:
                    now_pair = (nums[idx], nums[target_idx])
                    if now_pair != last_pair:
                        pair_count += 1
                        last_pair = now_pair
                    target_idx += 1
                else:
                    pass
                break

            # check target_idx
            if target_idx >= len_nums:
                break

        return pair_count

class Solution2(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        list_lookup_table = {}
        pair_count = 0
        for elem in nums:
            list_lookup_table[elem] = list_lookup_table.get(elem, 0) + 1

        for key, val in list_lookup_table.iteritems():
            if k == 0:
                if val >= 2:
                    pair_count += 1
            else:
                if list_lookup_table.get(key + k, 0) != 0:
                    pair_count += 1
        return pair_count

if __name__ == '__main__':
    sol = Solution2()

    print 3 == sol.findPairs([3,3,2,2,4,5,6], 2)
    print 2 == sol.findPairs([1,1,1,1,2,2,5], 0)
