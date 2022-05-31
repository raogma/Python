def balance_brackets(list, raw_data):
    if raw_data == '(':
        list.append(raw_data)
    elif raw_data == ')':
        list.append(raw_data)
        if '(' in list and len(list) == 2:
            list.clear()


n_lines = int(input())
brackets = list()

for _ in range(n_lines):
    balance_brackets(brackets, input())

print('BALANCED') if len(brackets) == 0 else print('UNBALANCED')
