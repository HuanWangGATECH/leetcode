class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indexDic={}
        for i in range(len(nums)):
            num=nums[i]
            complement=target-num
            if complement in indexDic:
                
                return [indexDic[complement],i]
            
            indexDic[num]=i
       
