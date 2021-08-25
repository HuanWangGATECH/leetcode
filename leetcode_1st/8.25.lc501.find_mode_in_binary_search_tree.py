# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        self.dict={}
        
        
        
        
        def dfs(node):
            
            if node:
                if node.val in self.dict:
                    self.dict[node.val]+=1 
                else:
                    self.dict[node.val]=1
            if node.left:
                dfs(node.left)
            
            if node.right:
                dfs(node.right)
                
                
            return 
                
            
            
            
        dfs(root)
        
        m=max(self.dict.values())
        
   
        ans=[]
        for i in self.dict.keys():
     
            if self.dict[i]==m:
                ans.append(i)
        return ans
            
        
