class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        
        ## creating 2 day array the right way 
        
        ## https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
        cols, rows = (m, n)
        ##arr = [[2]*cols]*rows wrong way
        
        arr = [[0 for i in range(rows)] for j in range(cols)]
    
        arr[0][0]=0
        
        print (arr)
        
        for i in range(1,m):
            arr[i][0]=1
        for j in range(1,n):
            arr[0][j]=1
        print (arr)
		# To reach every other square in the grid, we can come either from top or from left. 
		# Thus, the number of ways it can be reached is equal to:
		# ways to reach square on its left + ways to reach square on top of it:
        for i in range(1, n):
            for j in range(1, m):
                left = arr[j][i-1]
                top = arr[j-1][i]
                arr[j][i]=top+left
        return arr[-1][-1] # The bottom-right corner value is our solution
        
