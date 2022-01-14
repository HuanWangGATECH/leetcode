# Conflicting Appointments (medium)

Problem Statement 

Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Example 1:

Appointments: [[1,4], [2,5], [7,9]]

Output: false

Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.

Example 2:

Appointments: [[6,7], [2,4], [8,12]]

Output: true

Explanation: None of the appointments overlap, therefore a person can attend all of them.

Example 3:

Appointments: [[4,5], [2,3], [3,6]]

Output: false

Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.


```python 
def conflictingAppointment(arr):
    
    
    arr=sorted(arr)
    prebtime,preetime=0,0
    for btime,etime in arr:
        if btime<preetime:
            return False
        prebtime,preetime=btime,etime 
    
    return True 
    
 
def can_attend_all_appointments(intervals):
    intervals.sort(key=lambda x: x[0])
    start, end = 0, 1
    for i in range(1, len(intervals)):
        if intervals[i][start] < intervals[i-1][end]:
        # please note the comparison above, it is "<" and not "<="
        # while merging we needed "<=" comparison, as we will be merging the two
        # intervals having condition "intervals[i][start] == intervals[i - 1][end]" but
        # such intervals don't represent conflicting appointments as one starts right
        # after the other
        return False
    return True
    
    
print (conflictingAppointment([[2,4],[6,7],[8,12]]))

print (conflictingAppointment([[6, 7], [2, 4], [8, 12]]))

print  (conflictingAppointment([[4, 5], [2, 3], [3, 6]]))
```

https://leetcode.com/playground/27Yfg4Xd



