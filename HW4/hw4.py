import sys
import numpy as np
import pandas as pd

def load(fname):
    f = open(fname, 'r').readlines()
    n = len(f)
    ret = {}
    for l in f:
        l = l.split('\n')[0].split(',')
        i = int(l[0])
        ret[i] = {}
        for j in range(n):
            if str(j) in l[1:]:
                ret[i][j] = 1
            else:
                ret[i][j] = 0
    ret = pd.DataFrame(ret).values
    return ret

def get_tran(g):
    """
    get the transition matrix
    """
    # TODO
    graph = np.array(g, dtype=float)
    nodes = graph.shape[1]
    for node in range(nodes):
        non_zero_nbr = np.count_nonzero(graph[:, node])
        graph[:, node] = graph[:, node] / non_zero_nbr
    return graph

def cal_rank(t, d = 0.85, max_iterations = 1000, alpha = 0.001):
    """
    calculate the rank of every node
    """
    # TODO
    nbr_nodes = t.shape[1]
    R = np.random.rand(nbr_nodes, 1)
    R = R / np.linalg.norm(R, 1)
    R_zeros = np.ones(shape=(nbr_nodes, 1), dtype=float) / nbr_nodes

    nbr_iter = 0
    while nbr_iter < max_iterations:
        R_new = (1-d) * R_zeros + d * np.matmul(t, R)
        nbr_iter += 1

        if dist(R_new, R) <= alpha:
            break
        
        R = R_new

    return R_new

def save(t, r):
    """
    save the transition matrix, ranks to 1.txt, 2.txt
    """
    # TODO
    np.savetxt('1.txt', t, fmt='%.16f')
    np.savetxt('2.txt', r, fmt='%.16f')

def dist(a, b):
    return np.sum(np.abs(a-b))

def main():
    graph = load(sys.argv[1])
    transition_matrix = get_tran(graph)
    rank = cal_rank(transition_matrix)
    save(transition_matrix, rank)

if __name__ == '__main__':
    main()

