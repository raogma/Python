def permutations(txt, idx):
    if idx == len(txt):
        print(''.join(txt))
        return
    for i in range(idx, len(txt)):
        txt[idx], txt[i] = txt[i], txt[idx]
        permutations(txt, idx + 1)
        txt[idx], txt[i] = txt[i], txt[idx]


permutations(['a','b','c'], 0)
