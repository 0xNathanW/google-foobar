import unittest

# Trainer with fewer bananas will bet all their bananas.

# Trainers with the same numbers of bananas dont get paired up.

# Trainers with more bananas will always lose.

# Once a match begins, the trainers will play and exchange bananas until they each have the same number of bananas.
# We don't want this to happen

# We can pair trainers such that they play infinitely many times.

# function the returns pairs of trainers that will play infinitely many times.




def match(i, j):
    generations = 0
    while i != j and generations < 300:
        if i > j:
            i -= j
            j *= 2
        else:
            j -= i
            i *= 2
        generations += 1
    return True if generations > 250 else False
    

for i in range(1, 50):
    for j in range(1, 50):
        if not match(i, j):
            print("{i} and {j} are not infinite".format(i=i, j=j))






# class TestSolutions(unittest.TestCase):

#     def test_solution(self):
#         self.assertEqual(solution([1, 1, 1]), 1)
#         self.assertEqual(solution([1, 2, 3, 4, 5, 6]), 3)