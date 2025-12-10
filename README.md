# Mini Documentation

## To Do List
~~1. In the initialize(), make sure duplicate inputs are not appended and then decrement the edgeCount~~ <br>
~~1.1 Yeah, scrap that, just assume the user doesn't do duplicate edges, just proceed with standard inputs~~ <br>
~~2. Find a way to visualize the graph~~ <br>
3. If possible, list the edges that overlap <br>
4. **IF SUPER POSSIBLE**, suggest changes to our current graph <br>
5. Make Presentation PPT/Canva <br>

## Link to Canva (FP Proposal)
https://www.canva.com/design/DAG4XHMYC4A/wiBz02iJiYRmIO4jYPUGBw/edit?utm_content=DAG4XHMYC4A&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## Link to Canva (FP Report)
`Insert canva link here.`

## Link to our Graph Planarity Simulator:
https://isabelhyl.github.io/Graph-Planarity-Visual-Simulation/

## Reference
https://informatika.stei.itb.ac.id/~rinaldi.munir/Matdis/2024-2025/Makalah/Makalah-IF1220-Matdis-2024%20(156).pdf

## How to Use Our Code
1. Run the "planarityChecker_modified2.py" code in your VSCode or any editor <br>
2. Input the amount of vertices and hit ENTER <br>
3. Input the amount of edges and hit ENTER <br>
4. For every edge you have, type in the format of: u v, where u is a vertex and v is u's neighbor <br>

## Brief Intro to Problem
We're trying to check whether a circuit board can have no overlapping circuits. To do this, we check whether the circuit board is planar or not. So, for the code... Just get the input, create the graph, then simplify the graph by multiple means. After getting the simplest form of the graph, we check for a K3,3 or K5 subgraph. If a K3,3 or K5 subgraph exists, then it's not planar (meaning there's overlapping circuits). Otherwise, it is planar (meaning there isn't any overlapping circuits.)

<br>

Also, simplifying the graph means like, if your input has duplicates like :
```
1 2
1 2
```
Then you can just remove one of them. That applies to, uh,
```
1 2
2 1
```
Since we're working with undirected graph, meaning there's no need to declare the edge from both sides.
Additionally if there is a two-degree vertex who exists between two vertices, we can just remove that node and connect the two neighboring vertices.
```
1 - 2 - 3
```
can become
```
1 - 3
```
and it'll still be the same.

## K3,3 and K5 Graph
<img width="1095" height="493" alt="image" src="https://github.com/user-attachments/assets/8b6fc8db-5de6-4c80-a76e-bdb0733a6c2e" />

## Suggestion from Pak Ilham
1. During the FP Presentation, he'll ask you to explain how NetworkX is used
2. Try to code the visualization
3. Then show which edge overlaps
4. **IF SUPER POSSIBLE**, suggest corrections to the graph (as in add nodes and where)(plus points)

## Some Test Case 

**Test 1 to check whether EulerInequality() works**
```
3
5
1 2
2 1
3 2
1 2
3 1
```
*Note : We definitely need to remove duplicating edges before running the EulerInequality() cuz this graph is technically planar. Look at image below as to why.*
<img width="1047" height="695" alt="image" src="https://github.com/user-attachments/assets/25febdb6-a747-4797-ae44-7b1832568eb3" />

**Test 2 to correct the Euler Inequality**
```
3
3
1 2
2 3
3 1
```
The "e <= 2*v - 4" is actually kinda wrong as it says the test case above is not planar. So, we removed that. We haven't done the edge unification from Test Case 1 yet though.

**TEST CASE 3:** <br>
Input:
```
4
6
1 2
2 4
4 3
3 1
2 3
1 4
```
Expected Output:
```
How many vertices are in your graph? How many edges are in your graph? Input your edges:

There won't be any overlapping circuits! Yay!
```

<br>

**TEST CASE 4:** <br>
Input:
```
6
9
1 4
2 5
3 6
2 4
2 6
1 5
5 3
3 4
1 6
```
Expected Output:
```
How many vertices are in your graph? How many edges are in your graph? Input your edges:

Oh no, there will be overlapping circuits no matter what...
```

<br>

**TEST CASE 5:** <br>
Input:
```
5
10
1 2
2 4
4 5
5 3
3 1
1 4
1 5
2 3
2 5
3 4
```
Expected Output:
```
How many vertices are in your graph? How many edges are in your graph? Input your edges:

Oh no, there will be overlapping circuits no matter what...
```

<br>

**TEST CASE 6:** <br>
Input:
```
6
11
1 2
2 4
4 5
5 3
3 1
1 4
1 5
2 3
2 5
3 4
3 6
```
Expected Output:
```
How many vertices are in your graph? How many edges are in your graph? Input your edges:

Oh no, there will be overlapping circuits no matter what...
```

<br>

**TEST CASE 7:** <br>
Input:
```
7
11
1 4
2 5
3 6
2 4
2 6
1 5
5 3
3 4
1 6
4 7
7 6
```
Expected Output:
```
How many vertices are in your graph? How many edges are in your graph? Input your edges:

Oh no, there will be overlapping circuits no matter what...
```

<br>

**TEST CASE 8:** <br>
Input:
```
5
6
1 4
2 5
5 3
3 2
2 4
4 3
```
Expected Output:
```
How many vertices are in your graph? How many edges are in your graph? Input your edges:

There won't be any overlapping circuits! Yay!
```

<br>

**TEST CASE 9:** <br>
Input:
```
7
13
1 2
2 3
3 4
4 5
5 1
1 3
3 5
5 2
2 4
4 1
1 7
7 6
6 4
```
Expected Output:
```
How many vertices are in your graph? How many edges are in your graph? Input your edges:

Oh no, there will be overlapping circuits no matter what...
```

<br>

**TEST CASE 10:** <br>
Input:
```
6
10
1 6
6 5
5 1
1 3
3 4
4 1
2 3
2 5
5 3
2 4
```
Expected Output:
```
How many vertices are in your graph? How many edges are in your graph? Input your edges:

There won't be any overlapping circuits! Yay!
```

<br>
