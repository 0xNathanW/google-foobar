# Greatest common divisor.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_coprimes(a, b):
    x = gcd(a, b)
    return int(a/x), int(b/x)

def pair(a, b):
    c = 1 - (((a+1)/2)-1)*2
    i = 0
    while c <= b:
        if c == b:
            return False
        i += 1
        c += 2**i
    return True

def is_loop(i, j):  # Determines if i and j will form a loop.
    # Get coprime numbers.
    i, j = get_coprimes(i, j)
    if i%2 == 0 or j%2 == 0:
        return True
    return pair(i, j) if i < j else pair(j, i)

def solution(l):
    # Each trainer repersented by index
    # to solve the issue duplicates can cause.
    loops = {i: [j for j in range(len(l)) if is_loop(l[i], l[j])] for i in range(len(l))}
    isolated = 0    # counts trainers not matched.
    counted = [False] * len(l) # whether each trainer has been seen.
    while False in counted: # cycles until all trainers have been seen.
        min_idx = 0
        for i in range(1, len(l)):  # find trainer with least loops.
            if ((len(loops[i]) < len(loops[min_idx]) or counted[min_idx]) and not counted[i]):
                min_idx = i
        if ((len(loops[min_idx]) == 0) or 
        (len(loops[min_idx]) == 1 and loops[min_idx][0] == min_idx)) and not counted[min_idx]:
            # delete from other loops if isolated.
            for i in loops:
                if min_idx in loops[i]:
                    loops[i].remove(min_idx)
            counted[min_idx] = True
            isolated += 1
        else:
            min_match = loops[min_idx][0]
            for i in range(1, len(loops[min_idx])): # find adjacent vertex with least loops.
                if loops[min_idx][i] != min_idx and len(loops[loops[min_idx][i]])<len(loops[min_match]):
                    min_match = loops[min_idx][i]
            if not counted[min_match]:
                # remove matched trainers from other loops.
                for i in loops:
                    if min_match in loops[i]:
                        loops[i].remove(min_match)
                    if min_idx in loops[i]:
                        loops[i].remove(min_idx)
                counted[min_match] = True
                counted[min_idx] = True
    return isolated

solution([1, 3, 21, 19, 7, 13])