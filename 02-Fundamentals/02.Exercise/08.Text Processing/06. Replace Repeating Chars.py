txt = input()

sorted_txt = [txt[i] for i in range(len(txt) - 1) if txt[i] != txt[i + 1]]
sorted_txt.append(txt[-1])
print(''.join(sorted_txt))