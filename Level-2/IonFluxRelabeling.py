import unittest

def find_parent(root, floor, n):
    right_child = root - 1
    left_child = root - floor - 1
    if right_child == n or left_child == n:
        return root
    else:
        if n <= left_child:
            return find_parent(left_child, floor//2, n)
        else:
            return find_parent(right_child, floor//2, n)

def solution(h, s):
    root = 2**h - 1
    for i in range(len(s)):
        node = s[i]
        if node == root or node < 1:
            s[i] = -1
        else:
            s[i] = find_parent(root, root//2, node)
    return s




class TestSolutions(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution(5, [19, 14, 28]), [21, 15, 29])
        self.assertEqual(solution(3, [7, 3, 5, 1]), [-1, 7, 6, 3])
        self.assertEqual(solution(3, [1, 4, 7]), [3, 6, -1])
        self.assertEqual(solution(4, [1, 7, 12]), [3, 15, 13])
        self.assertEqual(solution(4, [6, 10, 5]), [7, 14, 6])
        

unittest.main()