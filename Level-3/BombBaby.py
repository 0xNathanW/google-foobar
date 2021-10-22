import unittest

def nxt_gen(m, f, g):
    if m == 1 and f == 1:
        return g
    if m > f:
        if m%f == 0:
            return g+m-1 if f==1 else "impossible"
        else:
            return nxt_gen(m%f, f, g+(m//f))
    if f > m:
        if f%m == 0:
            return g+f-1 if m==1 else "impossible"
        else:
            return nxt_gen(m, f%m, g+(f//m))
    else:
        return "impossible"

def solution(x, y):
    return str(nxt_gen(int(x), int(y), 0))




class TestSolutions(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution("4", "7"), "4")
        self.assertEqual(solution("2", "1"), "1")
        self.assertEqual(solution("2", "4"), "impossible")
        self.assertEqual(solution("1", "1"), "0")

#print(solution("4", "7"))
unittest.main()