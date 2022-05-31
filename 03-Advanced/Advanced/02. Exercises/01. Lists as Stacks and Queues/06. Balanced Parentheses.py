from collections import deque
line = deque(input())
brackets = {
    ']': '[',
    ')': '(',
    '}': '{',
    ' ': ' ',
}

opening_brckts = list()
isBalanced = True

while line:
    brckt = line.popleft()
    if brckt in brackets.values():
        opening_brckts.append(brckt)
    else:
        if opening_brckts:      # if input starts with closing brckt
            opening_brckt = opening_brckts.pop()
            if brackets[brckt] != opening_brckt:
                isBalanced = False
                print('NO')
                break
        else:
            isBalanced = False
            print('NO')
            break

if isBalanced:
    print('YES')
