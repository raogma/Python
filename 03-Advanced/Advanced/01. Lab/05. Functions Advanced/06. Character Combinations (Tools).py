from itertools import permutations

txt = input()
for x in permutations(txt, len(txt)):
    print(''.join(x))