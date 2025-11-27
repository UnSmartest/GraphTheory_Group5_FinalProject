# uh, what are the libraries again?
# networkX iirc
# oh yeah, this is undirected graph btw, i mean sure we can make it directed but eh we're not really designing it that way

# get the input
def initialize():
    print("How many vertices/electrical components do you have?")
    vertexCount = int(input())
    print("How many edges/electrical wires do you have?")
    edgeCount = int(input())
    listofEdges = []
    for listEdges in range(1, edgeCount+1):
        u = int(input())
        v = int(input())
        listofEdges.append(u, v)

# "first-line defense" as in like, who knows we can easily determine its planarity easily
def eulerInequality(vertexCount, edgeCount):
    v = vertexCount
    e = edgeCount
    if(e <= 2*v - 4 and e <= 3*v-6): return True
    return False

# int main(){}
initialize()
if(not eulerInequality()): 
    print("There will be overlapping circuits no matter what.")
    #how do you terminate program
    
isomorphicTo_K33_or_K5 = False
# but in case our graph passes the eulerInequality check, we move onto the second check (I3,3 & I5)
    # simplify the graph as much as possible by removing any duplicates (such as A → B and B → A, or if A → C and A → C then merge)
    # if a two-degree node exists between two nodes, remove said node and join its two neighbors
    # using NetworkX, check our simplified graph is isomorphic to a K3,3 or K5 graph
    # if it is, then isomorphicTo_K33_or_K5 = True
    
if(isomorphicTo_K33_or_K5):
    print("There will be overlapping circuits no matter what...")
else:

    print("There won't be any overlapping circuits! Yay!")
