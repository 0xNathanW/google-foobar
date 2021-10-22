import unittest

def solution(n):
    pass


class TestSolutions(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution(3), 1)
        self.assertEqual(solution(200), 487067745)
        self.assertEqual(solution(4), 1)
        self.assertEqual(solution(5), 2)


