import sys
import numpy as np
from graph_gen import *

def has_cycle(sets):
    # return True if the graph has cycle; return False if not
    graph_rep = np.array(sets)
    
    graph_rep_copy = graph_rep.copy()
    nbr_nodes = graph_rep.shape[0]

    while nbr_nodes > 0:
        graph_rep_copy = np.dot(graph_rep_copy, graph_rep)
        
        # check have >1 in diagonal value
        for i in range(nbr_nodes):
            if graph_rep_copy[i, i] >= 1:
                return True
        
        nbr_nodes -= 1
    return False

'''
    HINT: You can `print(sets)` to show what the matrix looks like
    If we have a directed graph with 2->3 4->1 3->5 5->2 0->1
            0  1  2  3  4  5
        0  0  1  0  0  0  0
        1  0  0  0  0  0  0
        2  0  0  0  1  0  0
        3  0  0  0  0  0  1
        4  0  1  0  0  0  0
        5  0  0  1  0  0  0
    The size of the matrix is (6,6)
'''

p2_list = get_p2("r07922072")
for sets in p2_list:
    if has_cycle(sets):
        print("YES")
    else:
        print("NO")
