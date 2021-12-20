import unittest

# function to solves test cases.
def solution(entrances, exits, path):
    throughput = 0
    btwn = [i for i in range(len(path)) if i not in entrances and i not in exits]
    for b in btwn:
        # check if b traces to an exit.
        for e in exits:
            if e in path[b]:
                
        throughput += c 
            
    print(throughput)
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

solution(
            [0], [3],
            [
                #0, 1, 2, 3
                [0, 7, 0, 0],#0 Entrance 
                [0, 0, 6, 0],#1   
                [0, 0, 0, 8],#2
                [9, 0, 0, 0] #3 Exit
            ],
        )