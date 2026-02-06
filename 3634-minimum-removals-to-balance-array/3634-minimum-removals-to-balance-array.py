class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        nums.sort()
        l=0
        best=0

        for r in range(len(nums)):
            while nums[l]*k<nums[r]:
                l+=1
            best=max(best,r-l+1)
        return len(nums)-best


        