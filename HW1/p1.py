import sys
import numpy as np
from graph_gen import *

def has_cycle(sets):
    # return True if the graph has cycle; return False if not
    graph_rep = np.array(sets)

    # find positin row, columns is 1
    for c in range(graph_rep.shape[1]):
        for r in range(graph_rep.shape[0]):

            if graph_rep[r, c] == 1:
                row_id = r
                col_id = c
            
                # find -1 with same columns, but diff row
                Is_addition = False
                for k in range(graph_rep.shape[0]):
                    if graph_rep[k, col_id] == -1:
                        Is_addition = True
                        addation = graph_rep[k] + graph_rep[row_id]
                        graph_rep = np.vstack((graph_rep, addation))
                
                if Is_addition:
                    graph_rep = np.delete(graph_rep, row_id, axis=0)

                # check have zero row or not
                All_zero = False
                for rr in range(graph_rep.shape[0]):
                    if sum(graph_rep[rr] == 0) == len(graph_rep[rr]):
                        All_zero = True
                        break
            
                if All_zero:
                    return True
    return False

'''
HINT: You can `print(sets)` to show what the matrix looks like
If we have a directed graph with 2->3 4->1 3->5 5->2 0->1
        0  1  2  3  4  5
    0  0  0 -1  1  0  0
    1  0  1  0  0 -1  0
    2  0  0  0 -1  0  1
    3  0  0  1  0  0 -1
    4 -1  1  0  0  0  0
The size of the matrix is (5,6)
'''

p1_list = get_p1("r07922072")
for sets in p1_list:
    if has_cycle(sets)
        print("YES")
    else:
        print("NO")

