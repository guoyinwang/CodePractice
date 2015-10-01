class Solution(object):
    def twoSum(self, nums, target):
        """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
        hashMap = {}
        length= len(nums)
        for i in range(0,length):
            if (target - nums[i]) in hashMap:
                return [hashMap[target - nums[i]]+1,i+1]
            else:
                hashMap[nums[i]] = i

        return [0,0]

if __name__=='__main__':
    nums = [3,2,4]
    target = 6
    a = Solution()
    result = a.twoSum(nums,target)
    print result