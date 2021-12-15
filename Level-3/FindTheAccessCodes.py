import unittest

def solution(l):
    mem = [0] * len(l)
    triples = 0
    if len(l) < 3:
        return 0
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            print("\n----------------------")
            print("i:", l[i], "j:", l[j])
            if l[j]%l[i] == 0:
                mem[j] += 1
                print(mem)
                triples += mem[i]
                print("added {num} to triples".format(num=mem[i]))
    print("\n============ end ===========")
    print(mem)
    return triples

class TestSolutions(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([1, 1, 1]), 1)
        self.assertEqual(solution([1, 2, 3, 4, 5, 6]), 3)

solution = solution([1, 2, 3, 4, 5, 6])