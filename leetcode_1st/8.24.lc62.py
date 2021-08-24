class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        unique_paths = [[1 for k in range(n)]] + [[1] for j in   range(m-1)]
        
		# To reach every other square in the grid, we can come either from top or from left. 
		# Thus, the number of ways it can be reached is equal to:
		# ways to reach square on its left + ways to reach square on top of it:
        for i in range(1, n):
            for j in range(1, m):
                left = unique_paths[j][i-1]
                top = unique_paths[j-1][i]
                unique_paths[j].append(left + top)
        return unique_paths[-1][-1] # The bottom-right corner value is our solution
        
