import unittest

def solution(s):
    colliders, total = 0, 0
    for i in s:
        if i == ">":
            colliders += 1
        elif i == "<":
            total += colliders * 2
    return total
        


class TestSolutions(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution(">----<"), 2)
        self.assertEqual(solution("<<>><"), 4)
        self.assertEqual(solution("-"), 0)
        self.assertEqual(solution(">>>>"), 0)
        self.assertEqual(solution("<<<"), 0)
        self.assertEqual(solution("--->-><-><-->-"), 10)

unittest.main()
