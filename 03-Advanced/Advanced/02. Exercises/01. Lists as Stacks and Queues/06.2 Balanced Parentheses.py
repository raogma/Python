line = input()

brackets = {
   '[': ']',
   '(': ')',
   '{': '}',
   ' ': ' ',
}

opening_brackets = list()
isBalanced = True

for symbol in line:
    if symbol in '{[(':
        opening_brackets.append(symbol)
    elif symbol in '}])':
        if opening_brackets:        #if line starts w/ closing brckt
            opening_bracket = opening_brackets[-1]
            if brackets[opening_bracket] != symbol:
                isBalanced = False
                break
            else:
                opening_brackets.pop()
        else:
            isBalanced = False
            break

if isBalanced:
    print('YES')
else:
    print('NO')