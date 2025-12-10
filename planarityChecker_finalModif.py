# only works for connected graphs
# disclaimer: while there is a nx.check_planarity function in network x, in this code we wanted to explore the inner logic behind the planarity checker algorithm

import networkx as nx
from networkx.algorithms import isomorphism
import itertools


def eulerInequality(e, n):
    if n <=4:
        # print("graph has 4 or less nodes: PLANAR")
        return 4 #a graph with 4 or less nodes is deffo planar so dont even bother
    # return e <= 3*n - 6 #krisna removed the 2n-4 thing
    return (e <= (2*n)-4) or (e<=(3*n)-6)
# isabel added back the 2n-4 thing hohoho

        

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
        # print("Elementary reduction: TRUE")
        return True
    #elif (g.number_of_nodes()>=5 and g.number_of_edges()>=7):
    # krisna also removed this criteria bcz it feels trippy to try to check if its nonseperable
    #    return False
    # print("Elementary reduction: SPECIAL CASE")
    return False
    

def contains_k5(g):
    if g.number_of_nodes() < 5:
        return False
    for subset_nodes in itertools.combinations(g.nodes(), 5):
        subgraph = g.subgraph(subset_nodes)
        if subgraph.number_of_edges()==10:
            return True
    return False

def contains_k33(g):
    if g.number_of_nodes() < 6:
        return False
    
    nodes_list = list(g.nodes())
    for subset_nodes_tuple in itertools.combinations(nodes_list, 6):
        subset_nodes = list(subset_nodes_tuple)
        
        node_anchor = subset_nodes[0]
        remaining_nodes = subset_nodes[1:] 
        
        for V1_tail_tuple in itertools.combinations(remaining_nodes, 2):
            V1 = set([node_anchor] + list(V1_tail_tuple))
            V2 = set(subset_nodes) - V1
            
            is_k33 = True
            for u in V1:
                for v in V2:
                    if not g.has_edge(u, v):
                        is_k33 = False
                        break
                if not is_k33:
                    break
            
            if is_k33:
                return True
                
    return False
        
    
def k5k33(g):
    if contains_k5(g):
        # print("CONTAINS K5")
        return True
    if contains_k33(g):
        # print("CONTAINS K33")
        return True
    # print("DOESNT CONTAIN K33 OR K5")
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


        
    # if graph has 4 or less nodes (from the euler inequality function too), planar (FIXED)
    # if euler's inequality = false, non planar (FIXED)    
    # if euler inequality = true, elementary reduction
    

    # if elementary reduction = true, planar (FIXED)
    # if elementary reduction = false, k33k5

    # if k33k5 = true, nonplanar (FIXED)
    # if k33k5 = false, planar (FIXED)


    # PLANARITY CHECKER STARTS HERE
    
    # euler's inequality
    euler_checker = eulerInequality(g.number_of_edges(), g.number_of_nodes())
    if not euler_checker:
        # print("Euler inequality: FALSE") # debug
        planar = False
        
    elif euler_checker == 4:
        planar = True

    else:
        # print("Euler inequality: TRUE") # debug
        # elementary reduction
        # er_result = elementaryReduction(g)
        #i(krisna) think we should do the checking on the original graph just in case...
        #so lets create a copy to modify(elementaryReduction)
        
        reduced_g = g.copy()
        if elementaryReduction(reduced_g):
            planar = True
        else:
            # k33 and k5
            if k5k33(reduced_g):
                planar = False
            else:
                planar = True
        
    
    # planar, P = nx.check_planarity(g)
    
    if planar:
        print("There won't be any overlapping circuits! Yay!")
    else:
        print("Oh no, there will be overlapping circuits no matter what...")


    # ACCURACY CHECKER (but why the FUCK is it saying that my fifth test case is planar, the fuck you mean)
    # is_planar, P = nx.check_planarity(g)
    # print(is_planar)

main()
