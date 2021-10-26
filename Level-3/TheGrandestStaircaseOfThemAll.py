import unittest

def solution(n):
    s = [[0]*n for r in range(n+1)]
    s[0][0] = s[1][1] = s[2][2] = 1
    for i in range(1, n):
        for j in range(n+1):
            s[j][i] = s[j][i-1]
            if j >= i:
                s[j][i] += s[j-i][i-1]
    return s[-1][-1]

class TestSolutions(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution(3), 1)
        self.assertEqual(solution(200), 487067745)
        self.assertEqual(solution(4), 1)
        self.assertEqual(solution(5), 2)


unittest.main()