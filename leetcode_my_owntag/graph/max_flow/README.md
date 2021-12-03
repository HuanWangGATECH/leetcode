# Max Flow Algorithms
General Max Flow Algorithm: ●Inputs: G(V,E), s, t, c
○ Directed graph G(V,E)
○ s,t∈V such that s is a source and t is a sink
○ c is capacities such that c(u,v) > 0 for (u,v) ∈ E ○ This set of inputs is also known as a Flow Network
● Outputs: f
○ f is a function for flow such that f(u,v) gives how much is sent through (u,v)
○ ∑f(·,t) is maximized.
○ C = ∑f(·,t)
○ We call C (sometimes called f*) the size of max flow.

● Steps:
1.Set f(u,v) = 0 for (u,v) ∈ E
2.Build a residual network Gf=(V,Ef)
3.Check for any path in Gf from s to t. ■Can use DFS or BFS
■ If none is found, we’re done.
4.If found, get the min capacity along path as cf(path)
5.Augment by cf(path) units along the path.
■ For each forward edge (u,v) along the path, increase f(u,v)
by cf(path) units
■ For each backwards edge (v,u) along the path, decrease
f(u,v) by cf(path) units 6.Recurse to step 2.
