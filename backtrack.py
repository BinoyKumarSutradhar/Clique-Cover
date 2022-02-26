import numpy as np
import math
import time
from itertools import combinations



test_graph = np.array([[0, 1, 0, 1, 1, 0],
                       [1, 0, 1, 0, 1, 0],
                       [0, 1, 0, 1, 1, 1],
                       [1, 0, 1, 0, 1, 1],
                       [1, 1, 1, 1, 0, 1],
                       [0, 0, 1, 1, 1, 0]])

def is_edge(u, v, adj_mat):
    return adj_mat[u-1, v-1] or adj_mat[v-1, u-1]

def is_clique(nodes, adj_mat):
    for (node_i, node_j) in combinations(nodes, 2):
        if not is_edge(node_i, node_j, adj_mat):
            return False
    return True


def cliques_from_list(nodes_list):
    v = len(nodes_list)
    cliques = dict()
    for i in range(v):
        clique = nodes_list[i]
        if clique in list(cliques):
            cliques[clique].add(i+1)
        else:
            cliques[clique] = set([i+1])
        
    return cliques

def is_solution(nodes_list, adj_mat):
    cliques_dict = cliques_from_list(nodes_list)
    for clique_nodes in cliques_dict.values():
        if not is_clique(clique_nodes, adj_mat):
            return False
    return True


def backtrack(adj_mat, cliques, v=1,  best=(math.inf, None)):
    n = adj_mat.shape[0]

    if v == n:
        if is_solution(cliques, adj_mat):
            if len(set(cliques)) < best[0]:
                best = (len(set(cliques)), cliques_from_list(cliques))

    else:
        for i in range(1, v+2):
            cliques[v] = i
            if is_solution(cliques, adj_mat):
                if len(set(list(cliques))) < best[0]:
                    best = backtrack(adj_mat, cliques, v+1, best)
    return best


def main():
    start_time = time.time()
    cliques = [0 for x in range(test_graph.shape[0])]
    cliques[0] = 1
    solution = backtrack(test_graph, cliques, 1)
    print(solution[0], "cliques:", solution[1])
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
