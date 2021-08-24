class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        if n<0: return 0
        if n==1: return 1
        if n==2: return 2
      
            
        result=[0]*(n+1)
        result[0]=0
        result[1]=1
        result[2]=2
      
        for i in range(3,n+1):
            
            #print (i)
            result[i]=result[i-1]+result[i-2]
            
        return result[n]
        
