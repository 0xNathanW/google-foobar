import unittest
from matplotlib import pyplot as plt
import itertools

# Trainer with fewer bananas will bet all their bananas.

# Trainers with the same numbers of bananas dont get paired up.

# Trainers with more bananas will always lose.

# Once a match begins, the trainers will play and exchange bananas until they each have the same number of bananas.
# We don't want this to happen

# We can pair trainers such that they play infinitely many times.

# function the returns pairs of trainers that will play infinitely many times.

# Method:

# 

# Performs a match between two trainers.
# Assumes infinite if over 250 generations.

## Psudo Code on condensed numbers a, b ##
# if a or b is even:
#     return infinite
# else:
#     take lowest number:
#         generate series of needed number for finite up to that number
#         if number is in series:
#             return finite
#         else: 
#             return infinite

def test_is_finite(i, j):
    generations = 0
    while i != j and generations < 300:
        if i > j:
            i -= j
            j *= 2
        else:
            j -= i
            i *= 2
        generations += 1
    return False if generations > 250 else True


def graph(nums):
    fig, ax = plt.subplots()
    for i in range(1, nums):
        for j in range(2, nums):
            if is_finite(i, j):
                ax.scatter(i, j, c='r', marker=".")
    plt.grid()
    plt.show()

# Greatest common divisor.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_goprimes(a, b):
    x = gcd(a, b)
    return int(a/x), int(b/x)

def pair(a, b):
    # a < b
    # sequence = 1 + 2^i
    c = 1 - (((a+1)/2)-1)*2
    i = 0
    while c <= b:
        if c == b:
            return True
        i += 1
        c += 2**i
    return False

def is_finite(i, j):
    # Get coprime numbers.
    i, j = get_goprimes(i, j)
    if i%2 == 0 or j%2 == 0:
        return False
    return pair(i, j) if i < j else pair(j, i)

def solution(l):
    for pairing in itertools.permutations(l, 2):
        print(pairing)
    pass



class Tests(unittest.TestCase):

    def test_rough(self):
        for x in range(1, 500):
            for y in range(1, 500):
                self.assertEqual(test_is_finite(x, y), is_finite(x, y))

unittest.main()