# Backtracing 

( I have done some problems using gmail logged in leetcode )

# leetcode list of problems 

https://leetcode.com/tag/backtracking


## permutations

    class Solution:
        def permute(self, nums: List[int]) -> List[List[int]]:
        
            res = []
            self.dfs(nums, [], res)
            return res
    
        def dfs(self, nums, path, res):
            if not nums:
                res.append(path)
            # return # backtracking
            for i in range(len(nums)):
                self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
            
            
 ## permutations2
 
 
     class Solution:
        def permuteUnique(self, nums: List[int]) -> List[List[int]]:
            res = []
            nums.sort()
            self.dfs(nums, [], res)
            return res
    
        def dfs(self, nums, path, res):
            if len(nums) == 0:
                res.append(path)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)
            
            
    
