import unittest
import sys

#range(1, (len(s)/2)+1):
def solution1(s):
    for i in [n for n in range(1, (len(s)/2)+1) if len(s)%n==0]:
        sub = s[:i]
        print("-"*10)
        print("subs", sub)
        for j in range(len(sub), len(s), len(sub)):
            nxt = s[j:j+len(sub)]
            print(nxt)
            if nxt != sub:
                print("{} not equal to {}".format(nxt, sub))
                break
        else:
            print("Answer found {}".format(len(s)/i))
            return len(s) / i

def solution(s):
    for i in [n for n in range(1, (len(s)/2)+1) if len(s)%n==0]:
        sub = s[:i]
        for j in range(len(sub), len(s), len(sub)):
            if s[j:j+len(sub)] != sub:
                break
        else:
            return len(s) / i
    else:
        return 1
            




class TestSolutions(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution("abcabcabcabc"), 4)
        self.assertEqual(solution("abccbaabccba"), 2)
        self.assertEqual(solution("aaaaaaaaaaaaaaaaaaaaaaaaaaa"), len("aaaaaaaaaaaaaaaaaaaaaaaaaaa"))
        self.assertEqual(solution("abcdefghijklmnop"), 1)

unittest.main()
# print("#######{}########".format(sys.version))
#solution("abccbaabccba")