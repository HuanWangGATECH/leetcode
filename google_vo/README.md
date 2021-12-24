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
  
  ## 6. https://www.1point3acres.com/bbs/thread-830242-1-1.html
  
  1st Interview: 11:15am-11:45am 还是同一个人 问BQ
（1）有没有主动做超过自己职责范围的工作
（2）在做project有没有遇到没有预想到的问题
（3）是什么一直激励你学习新的知识在CS领域
。。。还有一些记不清楚了
2nd Interview: 12:00pm-12:45pm
一个白人小哥 很nice 口音很清楚 太舒服了
以下内容需要积分高于 200 您已经可以浏览
反转链表
follow up 二维的链表 right 和 down两个指针 反转
3rd Interview: 1:00pm-1:45pm
一个阿三 体验感太差了 怎么这么mean 呢？ 我跟他说话压根不理我 我一般问第三遍才蹦出一个回答 给我搞得快哭了 这一轮特别差劲
给一个index 判断是否在complete binary tree里面 要求复杂度小于O(n) 想不出来就写了个O(n)的 哭了
4th Interview: 3:00pm-3:45pm
国人小哥 超级nice 一直笑呵呵 一直提示我 一直引导我 感觉像是带着我在做题的老师 hhh
就是我太紧张了 脑子想说“break 语句” 脱口 “we can broke up ”  太尴尬了😅
in order traverse binary tree
follow up: 判断两个树是否有相同的in order path 两个树的样子肯定不一定一样 要求同时遍历两个树
5th Interview: 4:00pm-4:45pm
判断不出来 只能说是亚洲人 超级新的题 我听了都懵逼了。。。
[hide=300]
card game
x shakes
y ranks
‍‌‍‌‍‌‌‍‌‍‍‌‍‍‍‍‌‌
Staright: must be 5 cards and same shakes and consecutive ranks for example: S1R2 S1R3 S1R4 S1R5 S1R6
given a list of string [S1R0, S2R7 .....] 找出能组成straight 的最大的 意思就是S的number大 R的number也大
要求比sort nlogn 复杂度好的算法
  
  
## 7. https://www.1point3acres.com/bbs/thread-829971-1-1.html
  
  
10/5 OA
11/5 VO
12/6 HR通知VO过了开始PA match，中间催过两次
12/8 PA match通过，口头offer
12/9 正式Offer
-------------VO面经--------------
5轮VO，一轮BQ+四轮代码，每轮45分钟，用的类似Google docs的平台写代码，不能compile也不能跑，面试官感觉不是特别苛求syntax上的准确度，只要算法准确半pseudo code也可以接受的样子，而且某些模糊的地方可以暂用black box function代替，就是定义一个功能性的function但是不需要具体写出来。四轮代码题的初始问题都是lc easy，follow up有些有lc median的难度，主要是需要及时的沟通
1 BQ：
一个白人小哥，简单寒暄之后发现他也很少给人面BQ，感觉和我一样紧张，问了5题左右，大概回答方针和亚麻家军规差不多，问题列表地里都有就不详细说了（主要是时间比较久远有点忘了），我回答的比较快所以后来又追问了一个简历上的项目经验
2 代码：
面试官是一个亚洲姐姐，问题很简单忘了，但是初始问题是比lc easy还要简单的那种，只记得用的binary search，follow up是在原题的基础上修改，涉及到一点sorting算法的问题，问了时空间复杂度。我在其中的一个follow up问题里在面试官表示已经过了之后找到了自己的一个bug并提出修改，面试官表示会在评价里加入这一点。
3 代码：
一个白人大哥
input是代表molecule的两个组成array，分别代表里面的atom和bond, 比如array A = ["H", "C", "H", "O"], B = [[0,1], [1,2], [1,3], [1,3]。 HCO分别是hydrogen, carbon, oxygen.问按照array B的链接方法是否组成一个valid molecule，其中H需要一条bond，C需要4条bond，O需要2条bond。最后组成的molecule大概是这样：
      O
      ||
H - C - H
follow up是问如果只计算每个atom的bond的数量，可能会存在单独分开的两个molecule，问如果检测这样的情况以及存在这样情况如何定义validness还有时空复杂度
4 代码：
白人小哥
初始问题是一个binary search
follow up 是用了他以前工作相关的问题，涉及到dfs+sorting算法
第二个followup 涉及到 multi-threading，不过不用写具体代码出来只要口头叙述
5 代码：
欧洲小哥
初始问题是graph theory，这题我搞砸了，确实是面太久脑子有点昏，花了很久才写出来
写之前被要求先说时空复杂度，一个是construct graph的时空复杂度，另一个是使用graph的复杂度
我写到一半发现原来说的不太对，只好跟他说我之前说错了construct graph应该是O(mn^2)
follow up还是graph得问题，不过修改题干之后要用不同的方式去建立初始的graph，时间不够了于是口头叙述算法
这一轮虽然算是写出来了但是比较勉强
总体体验是代码有小问题其实没关系，重点要思路正确以及对自己写的算法要足够理解（比如复杂度），VO前四轮的面试官都非常有耐心交流也很顺畅
个人感觉，包括HR推荐的都是要注重沟通，hr亲口说狗家面试官除了看你本身代码能力以外也作为和你合作的对象考察你和别人合作解决问题的能力，所以要把思路完整的说出来，卡壳尽管问，并不会被扣太多分。个人感觉如果不沟通只低头写代码，就算写对也不太会有很高的评价。
----------总结----------
面试体验已经hr沟通体验都很好，OA甚至有一题是Brute force解的，但依旧给了VO（可能今年比较缺人）.
VO总体难度不高，尤其‍‌‍‌‍‌‌‍‌‍‍‌‍‍‍‍‌‌是初始问题的难度都是lc easy, 有了初始的框架，follow up问题难度即使提升思路也会比较顺畅，我猜想是故意设计的面试流程以考察思路连贯性，沟通的积极性，以及尽可能降低刷题多的人的优势。
由于没有其他更好offer所以直接接了湾区的ng标准包，22年8月入职，同去湾区的可以加我！

  
  ## 8. https://www.1point3acres.com/bbs/thread-829038-1-1.html
  
  一共五轮，1 BQ + 4 tech
1. 第一轮BQ没什么特别的问题，正常BQ
2. trie的题，类似642
3. 给一个matrix，0代表可以走的路，1代表obstcle，问我们可以得到几个正方形。看附件图片，我用dp解的
4. 一道常规Permutation相关的dfs的题
5. 一道Word Break II 变形
总体感受无论下来还还是挺累的，建议在做的时候先讲思路和想到要用的数据结构和算法并且和面试官clarify清楚是否读懂题了，他是否赞成你的这个思路，然后再开始写。
做题期间卡住了，要积极的和面试官沟通，不要害怕问了就扣分，总比干脆‍‌‍‌‍‌‌‍‌‍‍‌‍‍‍‍‌‌做不出来强吧。
另一个感受就是基础要扎实，因为后续会有一些follow up。
补充内容 (2021-12-12 11:26 +8:00):
有童鞋说第三题是刷题网药而齐鳍，我看了一下真的是
