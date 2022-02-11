# Backtracing 

( I have done some problems using gmail logged in leetcode )

In this article, we introduce another paradigm called backtracking, which is also often implemented in the form of recursion.

Backtracking is a general algorithm for finding all (or some) solutions to some computational problems (notably Constraint satisfaction problems or CSPs), which incrementally builds candidates to the solution and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot lead to a valid solution. [1] 

![](backtracking)

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
                
                
 ## subsets with duplicates 
 
    class Solution:
        def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
            res=[]
        
            nums.sort()
        
            self.dfs(nums,[],res)
        
            return res
    
    
        def dfs(self,nums,path,res):
            res.append(path)
        
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue 
                self.dfs(nums[i+1:],path+[nums[i]],res)
                
                
## combination sum 

    class Solution:
        def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
            res=[]
            self.dfs(candidates,[],res,target)
        
            return res 
    
    
        def dfs(self,nums,path,res,target):
        
        
            #print ("dfs",nums,path,res)
            if sum(path)==target:
                res.append(path)
                return 
            elif sum(path)>target:
                return 
            else:
                for i in range(len(nums)):
                    self.dfs(nums[i:],path+[nums[i]],res,target)
            


## combination sum 2
    class Solution:
        def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
            candidates=sorted(candidates)
        
            res=[]
        
            self.dfs(res,[],candidates,target)
            return res 
        
        def dfs(self,res,path,candidates,target):
        
            if sum(path)==target:
                res.append(path)
                return 
            elif sum(path)> target:
                return 
        
            for i in range(len(candidates)):
                if i>0 and candidates[i]==candidates[i-1]:
                    continue
                self.dfs(res,path+[candidates[i]],candidates[i+1:],target)
