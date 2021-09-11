class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        start=intervals[0][0]
        end=intervals[0][1]
        result=[]
        for i in range(1,len(intervals)):
           
            interval=intervals[i]
            currStart=interval[0]
            currEnd=interval[1]
            print (start,end,currStart,currEnd)
            if currStart<=end:
                end=max(end,currEnd)
            else:
                print ("append")
                result.append([start,end])
                start=currStart
                end=currEnd
                
        result.append([start,end])        
        return result 
        
        
        
