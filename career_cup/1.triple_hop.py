
# a child is running up staircase with n steps and can hop 1 step 2 step or 3 steps at a time. Implement a method to count how many possible ways the child can run up stairs
# leetcode 70 . climbing stairs 

def triple_hop(x):
    if x < 0:
        return 0
    if x == 0:
        return 1
    if x == 1:
        return 1
    return triple_hop(x - 1) + triple_hop(x - 2) + triple_hop(x - 3)


if __name__ == "__main__":
    print(triple_hop(1))
    print(triple_hop(2))
    print(triple_hop(3))
    print(triple_hop(4))
    print(triple_hop(5))
    print(triple_hop(6))

    print(method_2(1))
    print(method_2(2))
    print(method_2(3))
    print(method_2(4))
    print(method_2(5))
    print(method_2(6))
    

    
    ### leetcode 70 solution 
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
  

### leetcode 70 using dictionary solution 
    
   class Solution:
    def climbStairsrec(self, num: int) -> int:
            if num == 1:
                return 1
            if num == 2:
                return 2
        
            if num in self.dct:
                return self.dct[num]
            else:
                self.dct[num] = self.climbStairsrec(num-1) + self.climbStairsrec(num-2)  
                
            return self.dct[num]
    
    
    def climbStairs(self, n: int) -> int:
        self.dct = {}
        return self.climbStairsrec(n)
