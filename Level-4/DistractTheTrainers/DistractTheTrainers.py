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
            if is_loop(i, j):
                ax.scatter(i, j, c='r', marker=".")
    plt.grid()
    plt.show()


def print_trainers(trainers):
    print("\nNode\tAdjacent Nodes")
    print("="*20)
    for i in trainers:
        print(i, "\t", trainers[i])
    print("\n")



#########################################################################

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
            return False
        i += 1
        c += 2**i
    return True

def is_loop(i, j):
    # Get coprime numbers.
    i, j = get_goprimes(i, j)
    if i%2 == 0 or j%2 == 0:
        return True
    return pair(i, j) if i < j else pair(j, i)

def search():
    pass
    

def solution(l):
    trainers = {}
    for i, j in itertools.combinations(l, 2):
        if is_loop(i, j):
            if i not in trainers:
                trainers[i] = {
                    "loops": [],
                    "counted": False
                }
            if j not in trainers:
                trainers[j] = {
                    "loops": [],
                    "counted": False
                }
            trainers[i]["loops"].append(j)
            trainers[j]["loops"].append(i)
    l.sort(key=lambda x: len(trainers[x]["loops"]))
    print(l)
    left = len(l)
    isolated = 0
    while left > 0:
        for i in l:
            print(f"checking {i}\n")
            if trainers[i]["counted"]:
                continue
            for j in l:
                if trainers[j]["counted"]:
                    continue
                if j in trainers[i]["loops"]:
                    trainers[i]["counted"] = True
                    trainers[j]["counted"] = True
                    left -= 2
                    break
            if not trainers[i]["counted"]:
                trainers[i]["counted"] = True
                isolated += 1
                left -= 1
            print_trainers(trainers)
    print("Isolated: ", isolated)
    return isolated

    
solution([1, 3, 21, 19, 21])