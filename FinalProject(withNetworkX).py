# dont forget to 
# pip install networkx
# (in case you havent lol)
import networkx as nx
G = nx.Graph()

# get the input
def initialize():

    print("How many vertices/electrical components do you have?")
    global vertexCount
    vertexCount = int(input())
    for vertexName in range(1, vertexCount+1):
        G.add_node(vertexName)

    print("How many edges/electrical wires do you have?")
    global edgeCount
    edgeCount = int(input())
    
    listofEdges = []
    print("Write your edge information! (1 2, to connect vertex 1 and 2)")
    for listEdges in range(1, edgeCount+1):
        u, v = map(int, input().split())
        #if the current (u, v) already exist in listofEdges, dont append it
        listofEdges.append((u, v))
    G.add_edges_from(listofEdges)

# "first-line defense" as in like, who knows we can easily determine its planarity easily
def eulerInequality(vertexCount, edgeCount):
    v = vertexCount
    e = edgeCount
    if(e <= 3*v-6): return True
    return False

# int main(){}
initialize()
if(not eulerInequality(vertexCount, edgeCount)): 
    print("There will be overlapping circuits no matter what.")
else:
    print("Your graph MIGHT be planar.")
    
# but in case our graph passes the eulerInequality check, we move onto the second check (I3,3 & I5)
    # simplify the graph as much as possible by removing any duplicates (such as A → B and B → A, or if A → C and A → C then merge)
    # if a two-degree node exists between two nodes, remove said node and join its two neighbors
    # using NetworkX, check our simplified graph is isomorphic to a K3,3 or K5 graph
    # if it is, then isomorphicTo_K33_or_K5 = True
# actually, do we really need to simplify the graph?
# eh sure, why not, later tho
    
K5 = nx.complete_graph(5)
K33 = nx.complete_bipartite_graph(3,3)
    
if(nx.is_isomorphic(G, K5) or nx.is_isomorphic(G, K33)):
    print("Oh no, there will be overlapping circuits no matter what...")
else:
    print("There won't be any overlapping circuits! Yay!")
