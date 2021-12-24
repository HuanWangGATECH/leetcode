## 1. NG https://www.1point3acres.com/bbs/thread-831287-1-1.html


12月初面的五轮狗狗

BQ：天竺姐姐 问了一堆有的没的，讲了讲自己实习时候的故事

VO1: 国人大哥，先是问了如何在树里找root到node的path，然后问从start node到end node的path如何找。这道题地里面经出现过好多次了

VO2: ABC姐姐，从定义leaf node和internal node开始实现一个rope，follow up是实现插入和删除某一段下标这两个method，第二个follow up就讲了个思路来不及写了

VO3: 国人姐姐，一个grid上面有房子和树，要求每一栋房子周围都要种1棵树，且所有树必须不同行不同列。follow up是如果同行或同列的有一个上限，怎么处理？这一轮回答的不好，follow up同样只来得及讲个思路

VO4: 东南亚姐姐，给一堆字符串，问能不能从每一个字符串选出一个字符，拼出target的字符串

蹭热度求问NG如何compete啊啊啊啊不想被狗lowball...实习结束拿到offer以‍‌‍‌‍‌‌‍‌‍‍‌‍‍‍‍‌‌后原地躺平，一直到11月份才想着要不要面一点公司。之前实习的return虽然从数字上比lowball高不少，但是毕竟已经过期了快三个月了...还有什么办法可以拿来和狗家compete吗？回复必加米！！

## 2. Intern https://www.1point3acres.com/bbs/thread-830949-1-1.html

一面：考的是排序和二分，三道题层层递进，前面两题口述算法和复杂度，只有最后一个问题需要写代码；

二面：考的是普通树删叶子，两个follw-up，分别是最新出现的叶子结点先删、最新出现的叶子结点后删


## 3. NG https://www.1point3acres.com/bbs/thread-831681-1-1.html

第一轮BQ 都是常规题（而且基本都忘了）就不写了

第二轮

Given training data as list of tokenized words
[[“I”, “am”, “a”, “person”],
   [“I”, “am”, “good”],
   [“a”, “person”]]
write a predictor that predict a word’s most frequent bigram
e.g. predict(“I”) -> “am”
  predict(“a”) -> “person
  predict(“am”) -> “a”
  
第三轮

Given a list of strings, a keyword, and an int N, print the words that are within distance N of the keyword
E.g. [“it”, “a”, “b”, “c”, “it”, “a”, “b”], keyword = “it”, N = 3
Output
it
a
b
c
it
a
b
followup: list变成stream

第四轮

先问了个简历上的BQ

Given an undirected graph that is also a ring that contains all vertices, find the ring
E.g. {0: [1,3], 1: [2, 0], 2:[1,3], 3:[0, 2]}, output [0,1,2,3] or [1,2,3,0] or [2,3,0,1] ….
感觉大部分‍‌‍‌‍‌‌‍‌‍‍‌‍‍‍‍‌‌时间都在写/讨论怎么check invalid input...

第五轮

面试官no show，过了几个小时回了email说有emergency...
求米！


## 4. https://www.1point3acres.com/bbs/thread-830661-1-1.html

1. bq: 基本问 teamwork 和 怎么 multitask (prioritize)..
2. 写出一个 id generator。不可以 3 个重复的号 （follow up: 如果换不能4个重复怎么改... 或是换成k..?）另外也 follow up 些 test case
3. Given list of object folder (有 id, name, parent id)。需要 output 每一个 folder 的 full path。(大约就是 parent path/name 这样）。然后 follow up 如何改正 optimize。
4. Given song list 和 int k。需要写个 function 随机选下一首歌。前提是不可以选 k last played song。
5. 给两个 string，看看 s1 是否可以加一个字母，然后重新排列组成 s2。follow up： 现在有 list<String> s1, 和 list<string> s2。每一个 s2 看看 s1 里是否有一个符合以上条件的 string, 然后 output list<boolean>。
感觉‍‌‍‌‍‌‌‍‌‍‍‌‍‍‍‍‌‌面试体验真的不错，跟面试官也都聊的不错。
大家加油！希望都拿到心仪的 offer~
找工不易，积分不够看不了一些帖子 😭
求加米!
  
## 5. https://www.1point3acres.com/bbs/thread-830277-1-1.html
  
  BQ天竺姐姐
1、和teammate有conflict
2、最让你骄傲的一个project
3、在team合作时候学到了什么
4、最大的challenge
5、有没有展现leadership的经历
6、未来3年内的打算
问了超多问题，直到超时5分钟她才发现，全程一直在打字，感觉应该面的不错？ 问题都准备到了，BQ的关键就在于多准备小故事，然后套到对应的问题上
最后反向BQ：如果有幸加入Google，能给我一些建议吗？
天竺姐姐：If you got an offer, please have confidence you deserve it.
这句话给我非常大的触动，非常感谢！
以下内容需要积分高于 188 您已经可以浏览
Coding轮开始
第一题，国人大哥
1.        Input: [1, 10 Alice] [1, 6 Bob] [5, 12 Cat] [15, 20 Dog]
Output:        1-5                Alice Bob
             5-6                Alice Bob Cat
             6-10        Alice Cat
            10-12        Cat
            15-20        Dog
非常像刷题网，meeting room的变种，最开始想的是用一个minHeap+一个maxHeap来做，但是中间具体implement的时候卡了半天，hint提示先sort，然后用双指针做，最后时间不够了，只是讲清楚了思路，连反向BQ也没来得及问，面的最差的一轮，没问到follow up，还好下一轮是午休之后，我反思了自己的问题，下午的状态就开始好起来了！
第二题，亚裔姐姐
2.        Input: “The    weather is good, and the   moon   is bright.”,
int colWidth：11
Output: “The weather”
             “is good, “
             “and the ”
             “the moon is”
             “bright.”
比较简单的String题目，具体思路是先把input转换成String array，然后不断更新colWidth，如果够放的话就继续放一个word，细节是如果这一行还够放一个space，换行前要放一个space，快速写好后让我提出更多test case，我问是否前后有更多spaces，以及word中间是否有超过一个space，她说是的，follow up就是解决这种situation，
Input: “      The    weather     is     good , and the   moon   is     bright.     ”, 快速修改了拿到String array的helper function就过了
反向BQ： A most challenging project in google？
亚裔姐姐：她说了一些关于project的东西，然后我们聊了聊Go语言的特性，拿到了亚裔姐姐的邮箱，应该也算面的不错
第三题，欧洲大哥
一上来先是问我知不知道什么是sweep keyboard，我说不知道，他给我解释了其实就是滑动输入
3.        Input: “bsdfsdfodewrwerewbsdfsdfsdfas”, List<String> words {boba, bobas, apple, happy, kit}
Output: first word(boba)
比较简单的dfs, 正常思路是用set做，但是我问了他words list的size，他说非常大，我就用trie做了，他可能也没想到我会用trie，问了我好多trie为什么用trie以及我写的trieNode class的细节问题。 快速写完之后是follow up：return the longest String
Output: Longest word(bobas)
这个也不难，保留一个global String，如果更长就更新。
反向BQ：你觉得在Google工作怎么样，喜欢吗？
欧洲大哥：前两年在amazon，今年刚过来，很喜欢这里的工作
然后我说我觉得Googler都特别酷，他说没有没有，我们都是普通人(有点***
这题也写的很快，而且用trie之后我感觉反馈特别好，也算面的不错
第四题，中东小哥
这是整个Google五轮中唯一一个问我自我介绍的，还好我背的比较牢，然后问我的背景，说我是不是开发过游戏，我说是的，他就说那我们来一道游戏的题目吧
先是一道简单的一维dp，一个游戏，每种move，需要turns，可以打出damage，最多x轮能打出的伤害
moves[[1,1][2,3][3,4][7,10]], turns 10  [turns, damage]
Output: max damage you can get
最近正好dp题目做的很多，学校里的算法课也一直学的dp，所以一上来先说了一个二维dp的做法，他说能不能只用一维dp，我就换了个思路，然后写完了
follow up：如果有些move会携带buff，持续y回合，当你有buff时，你造成的damage 双倍，
这个follow up是今天最难的一个了，当我讲完思路之后升级到二维dp后，他说没问题，就开始implement了，但是因为时间剩的不是很多，implement到一半的时候，
他说不用继续写了，到这一步已经better ‍‌‍‌‍‌‌‍‌‍‍‌‍‍‍‍‌‌than most candidates了，最后聊了两句就结束了，应该也算面的还可以
最后上timeline
10/25 OA
10/31 Interview prep call
11/19 5轮 VO
12/6 Team placement form
12/9 PA patch - GCP
12/10 Offer Approved
从VO开始到Offer正好三周整，碰到一个效率比较高的recruiter，面试的题目也不太难，运气还算比较好，中间一度觉得国人大哥的第一轮面的不是太好，但结果也过了
祝地里的小伙伴找工顺利! 如果觉得有帮助到的求加米，感谢！！~
