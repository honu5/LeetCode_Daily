class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        ans=[]
        cnt=0
        for i in nums:
            idx=0
            if i>0:
                idx+=(i+cnt)
                while(idx>(len(nums)-1)):
                    print(idx)
                    idx-=len(nums)
                ans.append(nums[idx])
                cnt+=1
            else: 
                idx+=(i+cnt)
                while(abs(idx)>(len(nums)-1)):
                    idx+=len(nums)
                ans.append(nums[idx])
                cnt+=1
        return ans 