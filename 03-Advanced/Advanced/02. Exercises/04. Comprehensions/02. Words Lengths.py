txt = input().split(', ')
txt_info = {element: len(element) for element in txt}
print(', '.join([f'{element} -> {txt_info[element]}' for element in txt_info]))
