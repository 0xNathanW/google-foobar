import unittest

def graph_print(path):
    for i in path:
        print(i)

def single_alt(enter, out, path):
    n = len(path)
    new_length = n + 2
    new_path = []
    for i in range(new_length):
        new_path.append([0] * new_length)
    for i in range(n):
        for j in range(n):
            new_path[i+1][j+1] = path[i][j]
    for i in enter:
        new_path[0][i+1] = float("Inf")
    for i in out:
        new_path[i+1][new_length-1] = float("Inf")
    graph_print(new_path)
    return 0, new_length - 1, new_path



#-------------------------------- Actual answer ----------------------------------#

from collections import deque

# bfs search, returns true if
def search(graph, s, t, parent):
    visited = set()
    q = deque()
    q.append(s)
    visited.add(s)
    while len(q) > 0:
        j = q.popleft()
        if j == t:
            return True
        for idx, v in enumerate(graph[j]):
            if idx not in visited and v > 0:
                q.append(idx)
                visited.add(idx)
                parent[idx] = j
    return False

def single_source_sink(enter, out, path):
    max_flow = float("Inf")
    # new singular source and sink.
    for i in path:
        i.insert(0, 0)
    path.insert(0, [0] * (len(path) + 1))
    for i in enter:
        path[0][i+1] = max_flow
    for i in path:
        i.append(0)
    path.append([0] * (len(path) + 1))
    for i in out:
        path[i+1][len(path)-1] = max_flow
    return 0, len(path) - 1, path

# solution implements ford-fulkerson algorithm for max-flow.
def solution(enter, out, path):
    enter, out, path = single_source_sink(enter, out, path)
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

            