
https://leetcode.com/explore/learn/card/recursion-i/

https://leetcode.com/explore/learn/card/recursion-ii/


# 分式简化

有一个同学在学习分式。他需要将一个连分数化成最简分数，你能帮助他吗？



连分数是形如上图的分式。在本题中，所有系数都是大于等于0的整数。

 

输入的cont代表连分数的系数（cont[0]代表上图的a0，以此类推）。返回一个长度为2的数组[n, m]，使得连分数的值等于n / m，且n, m最大公约数为1。

 

示例 1：

输入：cont = [3, 2, 0, 2]
输出：[13, 4]
解释：原连分数等价于3 + (1 / (2 + (1 / (0 + 1 / 2))))。注意[26, 8], [-13, -4]都不是正确答案。
示例 2：

输入：cont = [0, 0, 3]
输出：[3, 1]
解释：如果答案是整数，令分母为1即可。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/deep-dark-fraction
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


```python
class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        
        
        #num,den=self.fractionRecursive(0,cont)
        n,m=self.fractionIterative(cont)
        return n,m


    def fractionRecursive(self,i,cont):
        if i==len(cont)-1:
            return 1,cont[i]
        
        prevnum,prevden=self.fractionRecursive(i+1,cont)

        return prevden,cont[i]*prevden+prevnum


    def fractionIterative(self,cont):

        n=1
        m=cont[len(cont)-1]

        for i in range(len(cont)-2,-1,-1):
            #print (i)
            temp=m
            m=m*cont[i]+n
            n=temp 

        return (n,m)
```


# This is elegant! Recursive and iterative solutions to binary search tree problem  

https://leetcode.com/problems/search-in-a-binary-search-tree/solution/


```python
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or val == root.val:
            return root
        
        return self.searchBST(root.left, val) if val < root.val \
            else self.searchBST(root.right, val)
```

```python
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root is not None and root.val != val:
            root = root.left if val < root.val else root.right
        return root
```


# Example of recursion TLE (time limit exceeded)


https://leetcode.com/problems/pascals-triangle-ii/

# Top down recursive solution TLE 


```python

class Solution {
  private int getNum(int row, int col) {
    if (row == 0 || col == 0 || row == col) {
      return 1;
    }

    return getNum(row - 1, col - 1) + getNum(row - 1, col);
  }

  public List<Integer> getRow(int rowIndex) {
    List<Integer> ans = new ArrayList<>();

    for (int i = 0; i <= rowIndex; i++) {
      ans.add(getNum(rowIndex, i));
    }

    return ans;
  }
}
```


# Dp solution 

```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        
        dp=[[0 for j in range(i+1)] for i in range(rowIndex+1)]
        
        for i in range(rowIndex+1):
            dp[i][0]=1
            dp[i][-1]=1
         
        
        print (dp)
            
        for i in range(1,rowIndex+1):
            for j in range(1,i):
                
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                
        
        return dp[rowIndex]
        
```
