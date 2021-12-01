# Kruskal’s MST Algorithm
## Input:
○ Graph G = (V,E), connected, undirected; edge weights w
## Output:
○ A minimum spanning tree defined by the edges E MST 
## Runtime:
○ O(m log m) or simplified to O(m log n)
## Sort edges by weight. Grab the lightest available edge that will not create a cycle when added to the MST. Another way to look at this is to never add edges of vertices in the same component in the MST. Keep doing this until all edges that will not create a cycle are added. This happens at exactly n-1 edges.
## The more common of the MST algorithms. Gives a set of edges which is useful to construct the next input for a black box, or to compare to the original G.

![Dijkstra's](https://github.com/HuanWangGATECH/leetcode/blob/main/leetcode_my_owntag/graph/Minimal_spanning_tree/MST.png)

![MST](https://github.com/HuanWangGATECH/leetcode/blob/main/leetcode_my_owntag/graph/Minimal_spanning_tree/MST.png)
