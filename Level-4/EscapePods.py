import unittest

def graph_print(path):
    for i in path:
        print(i)

def search(graph, s, t, parent):
    visited = [False] * len(graph)
    q = [s]
    visited[s] = True
    while q:
        j = q.pop(0)
        for idx, v in enumerate(graph[j]):
            if not visited[idx] and v > 0:
                q.append(idx)
                visited[idx] = True
                parent[idx] = j
                if idx == t:
                    return True
    return False

# solution implements ford-fulkerson algorithm for max-flow.
def solution(enter, out, path):

    
    if len(enter) == 0 or len(out) == 0:    return 0
    max_in = float("Inf")
    if len(enter) == 1:  enter = enter[0]
    else:
        for i in path:
                i.insert(0, 0) 
        path.insert(0, [0] * (len(path) + 1)) 
        for i in enter:
            path[0][i+1] = max_in
        enter = 0
    if len(out) == 1:  out = out[0]
    else:
        if len(out) > 1: # dummy sink if multiple exits.
            for i in path:
                i.append(0)
            path.append([0] * (len(path) + 1))
            for i in out:
                path[i+1][len(path)-1] = max_in
            out = len(path) - 1
    graph_print(path)


    parent = [-1] * len(path) # stores path.
    throughput = 0
    while search(path, enter, out, parent): # while path from enter to out exists.
        residual_cap = float("Inf") # init as infinite.
        s = out
        while s != enter:
            residual_cap = min(residual_cap, path[parent[s]][s]) 
            s = parent[s]
        throughput += residual_cap # add flow to total throughput.
        v = out
        while v != enter:
            u = parent[v] 
            path[u][v] -= residual_cap # update residual graph.
            path[v][u] += residual_cap # update residual graph.
            v = parent[v] 
    return throughput

# between rooms can lead to each other.

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution(
            [0], [3],
            [
                #0, 1, 2, 3
                [0, 7, 0, 0],#0 Entrance 
                [0, 0, 6, 0],#1   
                [0, 0, 0, 8],#2
                [9, 0, 0, 0] #3 Exit
            ],
        ), 6)

        self.assertEqual(solution(
            [0, 1], [4, 5],
            [
                #0, 1, 2, 3, 4, 5
                [0, 0, 4, 6, 0, 0],#0 Entrance
                [0, 0, 5, 2, 0, 0],#2 Entrance
                [0, 0, 0, 0, 4, 4],#2
                [0, 0, 0, 0, 6, 6],#3
                [0, 0, 0, 0, 0, 0],#4 Exit
                [0, 0, 0, 0, 0, 0] #5 Exit
            ],
        ), 16)

unittest.main()