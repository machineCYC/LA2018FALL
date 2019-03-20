import numpy as np
import numpy.random as rand

def gen_graph(node_num, edge_num):
    graph_list = list()
    for _ in range(edge_num):
        while True:
            edge = rand.randint(0, node_num, 2)
            if edge[0] != edge[1]:
                graph_list.append(edge.tolist())
                break
    return graph_list

def gen_graph_list(size):
    graph_list = list()
    for _ in range(size):
        node_num = rand.randint(20, 60)
        edge_num = rand.randint(10, 50)
        graph_list.append(gen_graph(node_num, edge_num))
    return graph_list

def convert_p1(graph_list):
    p1_list = list()
    for graph in graph_list:
        node_num = np.max(graph)+1
        p1_matrix = list()
        for x, y in graph:
            row = [0] * node_num
            row[x] = -1
            row[y] = 1
            p1_matrix.append(row)
        p1_list.append(p1_matrix)
    return p1_list

def convert_p2(graph_list):
    p2_list = list()
    for graph in graph_list:
        node_num = np.max(graph)+1
        p2_matrix = np.zeros((node_num, node_num), dtype=int).tolist()
        for x, y in graph:
            p2_matrix[x][y] = 1
        p2_list.append(p2_matrix)
    return p2_list

def get_p1(seed):
    seed = int(seed[2:])
    rand.seed(seed*10+1)
    graph_list = gen_graph_list(12)
    return convert_p1(graph_list)

def get_p2(seed):
    seed = int(seed[2:])
    rand.seed(seed*10+2)
    graph_list = gen_graph_list(12)
    return convert_p2(graph_list)

