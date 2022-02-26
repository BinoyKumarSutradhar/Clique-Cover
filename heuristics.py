import numpy as np
import math
import time
import random
from itertools import combinations
from collections import defaultdict


test_graph = np.array([[0, 1, 0, 1, 1, 0],
                        [1, 0, 1, 0, 1, 0],
                        [0, 1, 0, 1, 1, 1],
                        [1, 0, 1, 0, 1, 1],
                        [1, 1, 1, 1, 0, 1],
                        [0, 0, 1, 1, 1, 0]])

def neighbors(nodes, adj_mat):
    neighbors = set()
    if isinstance(nodes, int):
        nodes = [nodes]
    for node in nodes:
        if node == 0:
            raise Exception("Node can't be 0: nodes are between 1 and N")

        for i in range(adj_mat.shape[0]):
            neighbor = adj_mat[node-1, i]
            if neighbor and (i != node):
                neighbors.add(i+1)
    return neighbors


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


def greedy(adj_mat, repetitions=10):
    n = adj_mat.shape[0]
 
    best = [x for x in range(1, n+1)]
    for r in range(repetitions):
        vertices = [x for x in range(1, n+1)]
        random.shuffle(vertices) 
        cliques = [0 for x in range(n)]
        sizes = defaultdict(int) 
        sizes[0] = n
        c = 1  
        for i in range(n):
            v = vertices[i]
            labeled = False
            neighbors_cliques = defaultdict(int)
            ret = neighbors(v, adj_mat)

            for neighbor in neighbors(v, adj_mat):
                neighbors_cliques[cliques[neighbor-1]] += 1
            for clique, size in neighbors_cliques.items():
                if size == sizes[clique]:
                    cliques[v-1] = clique
                    sizes[clique] += 1  
                    labeled = True
                    break
            if not labeled:
                cliques[v-1] = c
                sizes[c] += 1
                c += 1
        if len(set(cliques)) < len(set(best)):
            best = cliques
    return best


def main():
    start_time = time.time()
    solution = cliques_from_list(greedy(test_graph))
    print("--- %s seconds ---" % (time.time() - start_time))
    print(len(solution), "cliques:", solution)


if __name__ == "__main__":
    main()