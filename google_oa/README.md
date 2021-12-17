https://leetcode.com/discuss/interview-question/352460/Google-Online-Assessment-Questions

https://www.1point3acres.com/bbs/thread-803115-1-1.html

https://algo.monster/problems/google_online_assessment_questions




https://www.1point3acres.com/bbs/thread-828384-1-1.html

https://www.1point3acres.com/bbs/thread-829026-1-1.html

https://www.1point3acres.com/bbs/thread-827735-1-1.html

https://www.1point3acres.com/bbs/thread-822518-1-1.html


# 1 ng
![oa1](https://github.com/HuanWangGATECH/leetcode/blob/main/google_oa/google_oa1.jpg)

https://leetcode.com/playground/ey2GRaF7 my solution 

https://pastebin.com/0aCyexe1 someone else solution 


# 2 ng
![oa2](https://github.com/HuanWangGATECH/leetcode/blob/main/google_oa/google_oa2.jpg)

https://leetcode.com/playground/N3c7bwqK someone else solution 


https://leetcode.com/playground/6PkVDknd my own solution 

# 3 intern 
given an array consisting of N integers, returns the maximum possible number of pairs with the same sum. each array may belong to one pair only. (focus on the correctness, not the performance)
A = [1,9,8,100,2] -> 2 (A[0],A[1]) and (A[2], A[4])
A = [2,2,2,3] -> 1 (A[0], A[1])

![google_oa3](https://github.com/HuanWangGATECH/leetcode/blob/main/google_oa/google_oa8.jpg)

# 4 intern 

given a string s consisting of lowercase letters, return the longest consistent fragment which begins and ends with the same letter. if there are many possible answers, return the one starting‍‌‍‌‍‌‌‍‌‍‍‌‍‍‍‍‌‌ at the earliest position.
S = "cbaabaab" -> "baabaab"
S = "performance" -> "reformance"
S = "cba" -> "c"

![google_oa4](https://github.com/HuanWangGATECH/leetcode/blob/main/google_oa/google_oa7.jpg)


# 5 ng
![google_oa3](https://github.com/HuanWangGATECH/leetcode/blob/main/google_oa/google_oa3.jpg)
![google_oa3_2](https://github.com/HuanWangGATECH/leetcode/blob/main/google_oa/google_oa3_2.jpg)

# 6 ng

给定‍‌‍‌‍‌‌‍‌‍‍‌‍‍‍‍‌‌一个arr A，求|A[i] - A[j]| == |i - j|的最大值

# 7 ng 最长palindrome with pairs
["gh","bc","hg"]
返回 4 因为 "ghhg"

![google_oa7](https://github.com/HuanWangGATECH/leetcode/blob/main/google_oa/google_oa5.jpg)
![google_oa7_2](https://github.com/HuanWangGATECH/leetcode/blob/main/google_oa/google_oa5_2.jpg)


my solution. https://leetcode.com/playground/8PQCADDH

my new faster solution https://leetcode.com/playground/bYPXAHBy

# 8 ng 10 rods  
recently added leetcode https://leetcode.com/problems/rings-and-rods/

![google_oa8](https://github.com/HuanWangGATECH/leetcode/blob/main/google_oa/google_oa6.jpg)







一个是10个rod 红绿蓝的圈
另一个是回文串 之前好多帖子都有


rods + palindrome
第一题 给一个全是两位小写字母的array，返回最长的palindrome的长度. 比如[“kc”, “ck”, “ab”]就是4 因为“kcck”或“ckkc”最长
‍‌‍‌‍‌‌‍‌‍‍‌‍‍‍‍‌‌第二题 有0-9号的rod 如果一根rod上同时有RGB得一分 返回总分


solution others 

  class Solution:
      def countPoints(self, rings: str) -> int:

          rods=[set() for _ in range(10)]
          n=len(rings)
          for i in range(0,n,2):
              color=rings[i]
              rod=int(rings[i+1])
              rods[rod].add(color)
          return sum(len(s)==3 for s in rods)   
