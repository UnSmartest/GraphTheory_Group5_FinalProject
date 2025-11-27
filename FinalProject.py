# uh, what are the libraries again?
# import networkx as nx
# we'll think about using networkx later

# get the input
def initialize():
    print("How many vertices/electrical components do you have?")
    global vertexCount
    vertexCount = int(input())
    
    print("How many edges/electrical wires do you have?")
    global edgeCount
    edgeCount = int(input())
    
    listofEdges = []
    print("List your edge's connections! (x y)")
    for _ in range(edgeCount):
        u, v = map(int, input().split())
        listofEdges.append((u, v))
        
    # return vertexCount, edgeCount, listofEdges

# okay so, in cases where there are duplicating edges (1 2, 1 2, 2 1)
# we definitely need to merge them first, so i guess we should include like (if tuple like that already exist, dont include, but idk)
# we'll improve on that later
# "first-line defense" as in like, who knows we can easily determine its planarity easily
def eulerInequality(vertexCount, edgeCount):
    v = vertexCount
    e = edgeCount
    if(e <= 2*v - 4 and e <= 3*v-6): return True
    return False

# int main(){}
initialize()
if(not eulerInequality(vertexCount, edgeCount)): 
    print("There will be overlapping circuits no matter what.")
    #how do you terminate program
    quit()
    
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

# TEST 1 (to check whether eulerInequality() works)
# 3
# 5
# 1 2
# 2 1
# 3 2
# 1 2
# 3 1
