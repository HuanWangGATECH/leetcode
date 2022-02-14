https://leetcode.com/problems/permutations/discuss/18284/Backtrack-Summary%3A-General-Solution-for-10-Questions!!!!!!!!-Python-(Combination-Sum-Subsets-Permutation-Palindrome)


```python
    def combinationSum(self, candidates, target):
        def backtrack(tmp, start, end, target):
            if target == 0:
                ans.append(tmp[:])
            elif target > 0:
                for i in range(start, end):
                    tmp.append(candidates[i])
                    backtrack(tmp, i, end, target - candidates[i])
                    tmp.pop()
        ans = [] 
        candidates.sort(reverse= True)
        backtrack([], 0, len(candidates), target)
        return ans
```

# Would you mind explaining why we should append nums[:] and not nums? If nums[:] returns a modified copy, shouldn't nums be pointing to the modified object and hence is valid for append as well? Thanks in advance.


https://stackoverflow.com/questions/32448414/what-does-colon-at-assignment-for-list-do-in-python



https://www.geeksforgeeks.org/python-cloning-copying-list/


