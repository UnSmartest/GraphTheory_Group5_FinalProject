# only works for connected graphs

import networkx as nx
from networkx.algorithms import isomorphism



def eulerInequality(e, n):
    if n < 3:
        return True #a graph with 3 or less nodes is deffo planar so dont even bother
    return e <= 3*n - 6 #krisna removed the 2n-4 thing
        

def elementaryReduction(g):
    # remove self loops
    # remove a node with 1 degree only
    # 2-degree vertices can also be removed
    # parallel edges can be merged
    
    changed = True
    
    while changed:
        changed = False
        
        # self loops
        loops = list(nx.selfloop_edges(g))
        if loops:
            g.remove_edges_from(loops)
            changed = True
            
        # nx doesnt create parallel edges, so skip the "parallel edges" condition
        
        deg1_nodes = [node for node, deg in dict(g.degree()).items() if deg == 1]
        if deg1_nodes:
            g.remove_nodes_from(deg1_nodes)
            changed = True
        
        
        deg2_nodes = [node for node, deg in dict(g.degree()).items() if deg == 2]
        for node in deg2_nodes:
            neighbors = list(g.neighbors(node))
            if len(neighbors) == 2:
                u, v = neighbors
                g.add_edge(u, v)  # merge path of node u and v
                g.remove_node(node)
                changed = True
                
    # return g.number_of_edges(), g.number_of_nodes()
    if (g.number_of_edges()<=4): # krisna simplified it
        return True
    #elif (g.number_of_nodes()>=5 and g.number_of_edges()>=7):
    # krisna also removed this criteria bcz it feels trippy to try to check if its nonseperable
    #    return False
    return False
    
def contains_subgraph(G, H):
    GM = isomorphism.GraphMatcher(G, H)
    return GM.subgraph_is_isomorphic()

    
def k5k33(g):
    k5 = nx.complete_graph(5)
    k33 = nx.complete_bipartite_graph(3,3)

    if contains_subgraph(g, k5):
        return True
    if contains_subgraph(g, k33):
        return True

    return False

    

  
def main():
    g = nx.Graph()

    amountOfVertex = int(input("How many vertices are in your graph? "))
    amountOfEdge = int(input("How many edges are in your graph? "))
    print("Input your edges:\n")

    for i in range(amountOfEdge):
        temp = input()
        if temp == "0":
            break
        nodeA, nodeB = temp.split()
        g.add_edge(nodeA, nodeB)


        
        
    # if euler's inequality = false, non planar (FIXED)    
    # if euler inequality = true, elementary reduction

    # if elementary reduction = true, planar (FIXED)
    # if elementary reduction = false, k33k5

    # if k33k5 = true, nonplanar (FIXED)
    # if k33k5 = false, planar (FIXED)


    # euler's inequality
    if not eulerInequality(g.number_of_edges(), g.number_of_nodes()):
        planar = False

    else:
        # elementary reduction
        # er_result = elementaryReduction(g)
        #i(krisna) think we should do the checking on the original graph just in case...
        #so lets create a copy to modify(elementaryReduction)
        reduced_g = g.copy()
        if elementaryReduction(reduced_g):
            planar = True
        else:
            # k33 and k5
            if k5k33(g):
                planar = False
            else:
                planar = True

    # print(g)
    if planar:
        print("There won't be any overlapping circuits! Yay!")
    else:
        print("Oh no, there will be overlapping circuits no matter what...")


    # ACCURACY CHECKER (but why the FUCK is it saying that my fifth test case is planar, the fuck you mean)
    # is_planar, P = nx.check_planarity(g)
    # print(is_planar)

main()