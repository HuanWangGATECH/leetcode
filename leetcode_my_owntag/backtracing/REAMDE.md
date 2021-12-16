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
            
            
    ## subsets 
    
        class Solution:
            def subsets(self, nums: List[int]) -> List[List[int]]:
                def backtrack(first = 0, curr = []):
                    # if the combination is done
                    if len(curr) == k:  
                        output.append(curr[:])
                        return
                    for i in range(first, n):
                     # add nums[i] into the current combination
                        curr.append(nums[i])
                        # use next integers to complete the combination
                        backtrack(i + 1, curr)
                        # backtrack
                        curr.pop()
        
                output = []
                n = len(nums)
                for k in range(n + 1):
                    backtrack()
                return output
